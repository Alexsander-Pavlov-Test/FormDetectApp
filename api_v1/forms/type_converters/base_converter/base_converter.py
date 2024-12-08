from typing import Any, Iterator
from .abc import AbctractTypeConverter
from collections.abc import MutableMapping
from loguru import logger


class BaseTypeConverter(AbctractTypeConverter):
    """
    Базовый класс конвертера типов.

    Этот класс является Базовым и необоходим только для
    наследования.

    ### Для определения своего класса парсера нужно указать:

    - Переопределить :class:`BaseTypeConverter.convert`
    - Определить все необходимые методы:
        - `convert_date`;
        - `convert_phone`;
        - `convert_email`;
        - `convert_float`;
        - `convert_int`;
        - `convert_text`;

    Для примера смотрите :class:`parsers.type_converters.DefaultTypeConverter`
    """

    def __init__(self,
                 target: MutableMapping,
                 ) -> None:
        """
        Args:
            target (MutableMapping): Объект в котором необходимо \
                конвертировать типы данных. Объекта типа
                :class:`typing.MutableMapping`
        """
        self.contaiter = dict(target)
        self.type_checkers = (
            self.convert_date,
            self.convert_phone,
            self.convert_email,
            self.convert_float,
            self.convert_int,
            self.convert_text,
        )
        self._converted: bool = False

    @property
    def is_convert(self):
        return self._converted

    def _convert_types(self,
                       value: str
                       ) -> Any:
        logger.info(f'get value before {value}')
        for converter in self.type_checkers:
            convert = converter(value=value)
            if convert:
                logger.info(f'get value after {convert}')
                return convert

    def _normazire_value(self, value: str) -> str:
        logger.info(f'before normalize {value}')
        normalized_value = value.strip("'").strip('"').replace(' ', '+', 1)
        logger.info(f'after normalize {normalized_value}')
        return normalized_value

    def __getitem__(self, key: Any) -> Any:
        value = self.contaiter[key]
        return value

    def __setitem__(self, key: Any, value: Any) -> None:
        self.contaiter[key] = value

    def __delitem__(self, key: Any) -> None:
        del self.contaiter[key]

    def __len__(self) -> int:
        return len(self.contaiter)

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        if self.contaiter != other:
            return False
        return True

    def __iter__(self) -> Iterator:
        values = self.contaiter.items()
        for key, item in values:
            yield (key, item)

    def convert(self) -> MutableMapping:
        if not self._converted:
            for values in self:
                self[values[0]] = self._convert_types(
                    value=self._normazire_value(values[-1]),
                )
            self._converted = True
        return self.contaiter
