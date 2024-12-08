import json
from httpx import AsyncClient
from fastapi import status
import pytest

from api_v1.forms.dao import FormDAO


class TestAPI:
    """
    Тесты API
    """
    @pytest.mark.asyncio
    async def test_create_template(self,
                                   client: AsyncClient,
                                   create_form: dict[str, str],
                                   ):
        response = await client.put(
            url='/forms/create',
            json=create_form,
            )
        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.asyncio
    async def test_execute_template(self,
                                    client: AsyncClient,
                                    search_template: dict[str, str],
                                    ):
        query = '&'.join([f'{key}={value}'
                          for key, value
                          in search_template.items()])
        response = await client.post(f'/forms/get_form?{query}')
        json_data = json.loads(response.content.decode('utf-8'))
        assert response.status_code == status.HTTP_200_OK
        assert json_data == ['Test']

    @pytest.mark.asyncio
    async def test_execute_template_extra(self,
                                          client: AsyncClient,
                                          search_template: dict[str, str],
                                          ):
        search_template = search_template | {'some': 'some@mail.ru',
                                             'name_boss': 'Any',
                                             'phone_boss': '+74342434234',
                                             }
        query = '&'.join([f'{key}={value}'
                          for key, value
                          in search_template.items()])
        response = await client.post(f'/forms/get_form?{query}')
        json_data = json.loads(response.content.decode('utf-8'))
        assert response.status_code == status.HTTP_200_OK
        assert json_data == ['Test']

    @pytest.mark.asyncio
    async def test_delete_template(self,
                                   client: AsyncClient,
                                   ):
        name = {'name': 'Test'}
        instance = await FormDAO.find_item_by_args(**name)
        _id = instance['_id']
        response = await client.delete(
            f'/forms/delete/{str(_id)}',
        )
        assert response.status_code == status.HTTP_204_NO_CONTENT
