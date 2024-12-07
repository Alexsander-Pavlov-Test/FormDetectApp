from datetime import datetime
from typing import ClassVar

from pydantic import validate_email
from pydantic_core import PydanticCustomError

from .base_converter import BaseTypeConverter
from .base_converter.utils import raise_type_convert_error
from config import settings


class DefaultTypeConverter(BaseTypeConverter):
    """
    Конвертер типов по умолчанию.

    Неоходим для стандартного объема задач.

    ## Пример:
    ```python
    dict_ = dict(
        name='some_name',
        date='2020-11-1'
        price='3300.11,
        quantity='4',
    )
    converter = DefaultTypeConverter(value=dict_)
    converted_dict = converter.convert()
    converted_dict
    <<
    {
        name: 'text',
        date: 'date',
        price: 'float',
        quantity: 'int',
    }
    >>
    ```
    """

    pattern_types: ClassVar[tuple[str]] = (
        settings.DATE_FIELD,
        settings.PHONE_FIELD,
        settings.EMAIL_FIELD,
        settings.TEXT_FIELD,
    )

    @classmethod
    def convert_float(self, value: str):
        """
        Конвертирование строки в float
        """
        copy_value = value
        if not copy_value.find('.') == -1:
            try:
                copy_value = float(copy_value)
                return settings.FLOAT_FIELD
            except ValueError:
                pass
        return

    @classmethod
    def convert_int(self, value: str):
        """
        Конвертирование строки в int
        """
        copy_value = value
        try:
            copy_value = int(copy_value)
            return settings.INT_FIELD
        except ValueError:
            pass
        return

    @classmethod
    def convert_date(self, value: str):
        """
        Конвертирование строки в data формат
        """
        copy_value = value
        try:
            date_converting = datetime.strptime(
                copy_value,
                settings.DATE_FORMAT_PREFIX,
                )
            copy_value = date_converting.date()
            return settings.DATE_FIELD
        except ValueError:
            try:
                date_converting = datetime.strptime(
                    copy_value,
                    settings.DATE_FORMAT_DOT,
                    )
                copy_value = date_converting.date()
                return settings.DATE_FIELD
            except ValueError:
                pass
        return

    @classmethod
    def convert_email(self, value):
        copy_value = value
        try:
            validate_email(copy_value)
            return settings.EMAIL_FIELD
        except PydanticCustomError:
            return

    @classmethod
    def convert_phone(self, value):
        copy_value = value
        copy_value = copy_value.replace(' ', '')
        if (copy_value.startswith('+') and
           copy_value.replace('+', '').isdigit()
           and len(copy_value) > 11):
            return settings.PHONE_FIELD

    @classmethod
    def convert_text(self, value):
        return settings.TEXT_FIELD

    def get_for_pattern(self):
        """
        Получение словаря по принципу паттерна

        Это означает что выведется словарь только с
        значениями `date`, 'phone', 'email', 'text'
        """
        if not self._converted:
            self.convert()
        pattern_dict = dict()
        for values in self:
            if values[-1] in self.pattern_types:
                pattern_dict[values[0]] = values[-1]
        return pattern_dict


class TypeChecker(BaseTypeConverter):
    """
    Класс проверки типов целевого объекта
    """
    allow_types: ClassVar[tuple[str]] = (
        settings.DATE_FIELD,
        settings.PHONE_FIELD,
        settings.EMAIL_FIELD,
        settings.FLOAT_FIELD,
        settings.INT_FIELD,
        settings.TEXT_FIELD,
    )

    def _type_check(self, value) -> bool:
        return value in self.allow_types

    @classmethod
    def convert_date(self, value):
        if not self._type_check(self, value):
            raise_type_convert_error(value, str(self.allow_types))

    @classmethod
    def convert_phone(self, value):
        if not self._type_check(self, value):
            raise_type_convert_error(value, str(self.allow_types))

    @classmethod
    def convert_email(self, value):
        if not self._type_check(self, value):
            raise_type_convert_error(value, str(self.allow_types))

    @classmethod
    def convert_float(self, value):
        pass

    @classmethod
    def convert_int(self, value):
        pass

    @classmethod
    def convert_text(self, value):
        if not self._type_check(self, value):
            raise_type_convert_error(value, str(self.allow_types))
