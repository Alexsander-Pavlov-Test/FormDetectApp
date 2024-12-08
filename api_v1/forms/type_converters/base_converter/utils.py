from typing import Any

from .exeptions import TypeConvertError


def raise_type_convert_error(value: Any, type_: Any) -> None:
    """
    Вызов исключения TypeConvertError
    """
    raise TypeConvertError(f'Значение {value} может быть только одним из '
                           f'{type_}')
