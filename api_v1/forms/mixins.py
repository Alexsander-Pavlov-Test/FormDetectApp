from loguru import logger
from api_v1.forms.utils import construct_key_value_dictionaries


class FindPrefechFormMixin:
    """
    Миксин который добавляет вспомогательные
    методы для запросов к БД
    """

    def check_is_right_form(self,
                            pattern: dict[str, str],
                            document: dict[str, str],
                            ) -> bool:
        """
        Проверка корректности формы
        Метод проверяет схождение ключа и значения

        В случае если количество схождений больше или ровно
        сумме длинны документа с которым сравнение, считается что
        форма корректна для использования

        Args:
            pattern (dict[str, str]): Введенная форма
            document (dict[str, str]): Шаблон формы

        Returns:
            bool: Корректно или нет
        """
        couter = 0
        for key, value in pattern.items():
            if key not in document or value != document[key]:
                pass
            else:
                couter += 1
        logger.info(f'equal between pattern {pattern} and document {document}')
        logger.info(f'count of coincidences {couter} in {document}')
        return len(document) <= couter

    @classmethod
    async def get_prefetch_name_form_by_args(cls,
                                             **kwargs,
                                             ) -> list[str]:
        """
        Выборка найболее подходящих имен форм для
        указанных атрибутов

        Returns:
            list[str]: Список имен
        """
        pattern = kwargs.copy()
        list_values = construct_key_value_dictionaries(pattern)
        logger.info(f'values to send query db {list_values}')
        list_objects = cls.model.find({"$or": list_values})
        form_names: list[str] = []
        for document in await list_objects.to_list():
            name = document.pop('name')
            document.pop('_id')
            logger.info(f'get document to check {document}')
            if cls.check_is_right_form(cls, kwargs, document):
                form_names.append(name)
        return form_names
