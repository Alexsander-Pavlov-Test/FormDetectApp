import asyncio
import httpx
import pytest
from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from bson.objectid import ObjectId
import pytest_asyncio

from api_v1.routers import register_routers
from config import settings


@pytest.fixture(scope='session', autouse=True)
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope='session', autouse=True)
async def app() -> AsyncGenerator[LifespanManager, Any]:
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        yield

    app = FastAPI(docs_url=None,
                  redoc_url=None,
                  lifespan=lifespan,
                  )
    register_routers(app=app)

    async with LifespanManager(app) as manager:
        yield manager.app


@pytest_asyncio.fixture(scope='session')
async def client(app: FastAPI) -> AsyncGenerator[httpx.AsyncClient, Any]:
    current_home = settings.CURRENT_ORIGIN
    current_api = settings.API_PREFIX
    async with httpx.AsyncClient(
        app=app,
        base_url=current_home + current_api,
    ) as client:
        yield client


@pytest.fixture
def dictionary():
    return dict(_id=ObjectId('67543b74156c9dedf8334542'),
                name='some_name',
                value='email',
                value_2='phone',
                )


@pytest.fixture
def dictionary_to_convert():
    return dict(
        name='some',
        phone='+7 913 553 1120',
        email='some@yandex.ru',
        date1='1990-01-20',
        date2='20.01.1990',
        integer='33',
        float_='44.2',
    )


@pytest.fixture
def converted_dictionary():
    return dict(
        name='text',
        phone='phone',
        email='email',
        date1='date',
        date2='date',
    )


@pytest.fixture
def create_form():
    return dict(name='Test',
                params=dict(
                    phone='phone',
                    email='email',
                    date1='date',
                    date2='date',
                ))


@pytest.fixture
def search_template():
    return dict(
        phone='+7 900 624 1000',
        email='good@yandex.ru',
        date1='2024-01-01',
        date2='01.01.2024',
    )
