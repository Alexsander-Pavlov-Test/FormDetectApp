from fastapi import APIRouter, HTTPException, status
from api_v1.forms.dao import FormDAO
from api_v1.forms.crud import CreateForm, ViewForm, DeleteForm

from api_v1.forms.type_converters import TypeChecker
from api_v1.forms.type_converters.base_converter.exeptions import TypeConvertError


router = APIRouter(prefix='/forms',
                   tags=['Forms'],
                   )


@router.get(path='/list',
            description='View List templates',
            response_model=list[ViewForm],
            response_model_by_alias=True,
            )
async def list_forms_templates():
    return await FormDAO.find_all_items_by_args()


@router.put(path='/create',
            description='Create your template',
            response_model=ViewForm,
            response_model_by_alias=True,
            status_code=status.HTTP_201_CREATED,
            )
async def create_form_template(form: CreateForm):
    model = form.model_dump()
    try:
        TypeChecker(target=model).convert()
    except TypeConvertError as ex:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=ex.args)
    result = await FormDAO.add(**model)
    return result


@router.delete(path='/delete/{id}',
               description='Delete template',
               status_code=status.HTTP_204_NO_CONTENT,
               )
async def delete_form_template(id: str):
    schema = DeleteForm(**{'_id': id})
    print(schema)
    await FormDAO.delete(schema.id)
