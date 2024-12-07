from pydantic import BeforeValidator, Field
from typing import Annotated
from bson.objectid import ObjectId

from config.models import FormSchema


StrObjectIdField = Annotated[ObjectId | str,
                             BeforeValidator(lambda arg: str(arg)),
                             ]
ObjectIdFieldFormStr = Annotated[ObjectId | str,
                                 BeforeValidator(lambda arg: ObjectId(arg)),
                                 ]


class CreateForm(FormSchema):
    """
    Создание формы
    """
    name: str


class ViewForm(CreateForm):
    """
    Просмотра формы
    """
    id: StrObjectIdField = Field(alias='_id')
    name: str


class DeleteForm(FormSchema):
    """
    Удаление формы
    """
    id: ObjectIdFieldFormStr = Field(alias='_id')
