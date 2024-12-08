from pydantic import BeforeValidator, Field, BaseModel
from typing import Annotated
from bson.objectid import ObjectId

from config.models import FormSchema


StrObjectIdField = Annotated[ObjectId | str,
                             BeforeValidator(lambda arg: str(arg)),
                             ]
ObjectIdFieldFormStr = Annotated[ObjectId | str,
                                 BeforeValidator(lambda arg: ObjectId(arg)),
                                 ]


class ParamsFormCreation(FormSchema):
    """
    Параметры для создания формы
    """


class CreateForm(BaseModel):
    """
    Создание формы
    """
    name: str
    params: ParamsFormCreation


class ViewForm(FormSchema):
    """
    Просмотр формы
    """
    id: StrObjectIdField = Field(alias='_id')
    name: str


class GetFormConvertSchema(FormSchema):
    """
    Схема получения конвертированной формы
    """


class DeleteForm(FormSchema):
    """
    Удаление формы
    """
    id: ObjectIdFieldFormStr = Field(alias='_id')
