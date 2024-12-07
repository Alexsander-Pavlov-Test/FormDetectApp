from pydantic import BeforeValidator, Field
from typing import Annotated
from bson.objectid import ObjectId

from config.models import FormSchema


ObjectIdField = Annotated[ObjectId | str, BeforeValidator(lambda arg: str(arg))]


class CreateForm(FormSchema):
    """
    Создание формы
    """
    name: str


class ViewForm(CreateForm):
    """
    Просмотра формы
    """
    id: ObjectIdField = Field(alias='_id')
    name: str
