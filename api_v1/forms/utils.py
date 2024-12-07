from bson.objectid import ObjectId


class ConvertObjectIDMixin:
    """
    Миксин конвертации `_id` в `id`

    Данный миксин (класс-примесь) не меняет изначальный
    объект, а возвращает новый.
    """

    def convert_id(self,
                   dictionary: dict[str, str | ObjectId],
                   ) -> dict[str, str]:
        """
        Конветрация :class:`bson.objctid.ObjctId`,
        а так же подмена ключа `_id` на `id`

        Args:
            dictionary (dict[str, str  |  ObjectId]): Целевой словарь\
                предположительно с ключем `_id`

        Returns:
            dict[str, str]: Измененный словарь если был `id`

        ## Пример
        ```python
        dict_ = dict(
            _id=ObjectId('67543b74156c9dedf8334542'),
            name='some_name',
        )
        mixin = ConvertObjectIDMixin()
        new_dict_ = mixin.convert_id(dict_)
        # >>
        new_dict_ -> {
            id='67543b74156c9dedf8334542',
            name='some_name',
        }
        # <<
        ```
        """
        copy_dict = dictionary.copy()
        if '_id' in copy_dict:
            copy_dict['id'] = str(copy_dict.pop('_id'))
        return copy_dict
