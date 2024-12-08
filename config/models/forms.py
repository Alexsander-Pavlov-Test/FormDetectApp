from pydantic import BaseModel, ConfigDict


class FormSchema(BaseModel):
    """
    Схема формы
    """
    model_config = ConfigDict(title='BaseFormSchema',
                              extra='allow',
                              arbitrary_types_allowed=True,
                              )
