from fastapi import APIRouter, Depends, status
from api_v1.forms.dao import FormDAO
from api_v1.exeptions import ValidationError
from api_v1.forms.crud import CreateForm, ViewForm


router = APIRouter(prefix='/forms',
                   tags=['Forms'],
                   )


@router.post(path='/create',
             description='Create your template',
             response_model=ViewForm,
             response_model_by_alias=True,
             )
async def create_form_template(form: CreateForm):
    result = await FormDAO.add(**form.model_dump())
    return result
