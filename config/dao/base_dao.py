from motor.motor_asyncio import AsyncIOMotorCollection
from bson.objectid import ObjectId
from typing import ClassVar

from config.dao.dao_types import MongoType


class BaseDAO:
    """
    Базовый DAO класс для CRUD модели

    Универсальный класс для легкого опеределения

    CRUD модели

    Для реализации DAO определенной модели необходимо:
    - Наследоваться от данного класса
    - Переопределить атрибут класса `BaseDAO.model`

    ## Примеры:
    ```python
    # Создание
    values = dict(
        name='some_name',
        some_value='some_value',
    )
    item = await FormDAO.add(values)
    item = await FormDAO.find_item_by_args(
        values,
    )
    items = await FormDAO.find_all_items_by_args(
        values,
    )
    ```
    """

    model: ClassVar[AsyncIOMotorCollection | None] = None

    @classmethod
    async def find_item_by_args(cls,
                                **kwargs: dict[str, str],
                                ) -> MongoType:
        """
        Нахождение и возращение сущности

        Returns:
            MongoType: Сущность из выборки
        """
        result = await cls.model.find_one(kwargs)
        return result

    @classmethod
    async def find_all_items_by_args(cls,
                                     **kwargs: dict[str, str | int],
                                     ) -> list[MongoType]:
        """
        Нахождение и возращение множества сущностей

        Returns:
            list[MongoType]: Сущности из выборки
        """
        list_objects = []
        async for object_ in cls.model.find(kwargs):
            list_objects.append(object_)
        return list_objects

    @classmethod
    async def add(cls,
                  **values,
                  ) -> MongoType:
        """
        Создание и возвращение сущности из базы данных
        """
        created_object = await cls.model.insert_one(values)
        new_object = await (cls.model
                            .find_one(dict(_id=created_object.inserted_id)))
        return new_object

    @classmethod
    async def delete(cls,
                     _id: ObjectId,
                     ) -> None:
        """
        Удаление сущности по ID
        """
        await cls.model.delete_one(dict(_id=_id))
