from abc import ABC, abstractmethod
from collections.abc import MutableMapping
from typing import Any


class AbctractTypeConverter(ABC, MutableMapping):
    """
    Абстрактный класс конвертера типов
    """

    @classmethod
    @abstractmethod
    def convert_float(self,
                      value: str,
                      ) -> Any:
        pass

    @classmethod
    @abstractmethod
    def convert_int(self,
                    value: str,
                    ) -> Any:
        pass

    @classmethod
    @abstractmethod
    def convert_date(self,
                     value: str,
                     ) -> Any:
        pass

    @classmethod
    def convert_text(self,
                     value: str,
                     ) -> Any:
        pass

    @classmethod
    def convert_phone(self,
                      value: str,
                      ) -> Any:
        pass

    @classmethod
    def convert_email(self,
                      value: str,
                      ) -> Any:
        pass

    @abstractmethod
    def convert(self) -> MutableMapping:
        pass
