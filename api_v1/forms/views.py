from fastapi import APIRouter, HTTPException, status, Request
from loguru import logger
from api_v1.forms.dao import FormDAO
from api_v1.forms.schemas import (
    CreateForm,
    ViewForm,
    DeleteForm,
    GetFormConvertSchema,
    )

from api_v1.forms.type_converters import TypeChecker, DefaultTypeConverter
from api_v1.forms.type_converters.base_converter.exeptions import TypeConvertError
from api_v1.forms.utils import construct_list_names

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
    params = model.pop('params')
    if not params:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Params for creation form cant be empty',
                            )
    try:
        TypeChecker(target=params).convert()
    except TypeConvertError as ex:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=ex.args)
    result = await FormDAO.add(**(model | params))
    return result


@router.post(path='/get_form',
             name='Form executer',
             description='Get Name form template. '
             '`Note!` Best to request form with `Postman`!',
             response_model=list[str] | GetFormConvertSchema,
             response_model_exclude=('_id',)
             )
async def get_form_template(request: Request):
    params = request.query_params._dict
    logger.info(f'get query params {params}')
    name = {}
    if not params:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Query params is empty, '
                            'you need to choise form like: '
                            '?name=param&name2=param2')
    converter = DefaultTypeConverter(params)
    pattern_types = converter.get_for_pattern()
    if 'name' in pattern_types:
        name['name'] = pattern_types.pop('name')
    if pattern_types:
        forms = await FormDAO.get_prefetch_name_form_by_args(**pattern_types)
        if not forms:
            pass
        else:
            return forms
    converted_types = converter.convert()
    return converted_types | name


@router.delete(path='/delete/{id}',
               description='Delete template',
               status_code=status.HTTP_204_NO_CONTENT,
               )
async def delete_form_template(id: str):
    schema = DeleteForm(**{'_id': id})
    print(schema)
    await FormDAO.delete(schema.id)
