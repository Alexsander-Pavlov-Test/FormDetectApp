import pytest
from bson.objectid import ObjectId


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
