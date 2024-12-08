from config.dao.dao_types import MongoType


def construct_list_names(execute_list: list[MongoType]) -> list[str]:
    """
    Функция собирает список имен форм

    Args:
        execute_list (list[MongoType]): Выборка из базы данных

    Returns:
        list[str]: Список имен
    """
    list_forms = []
    for item in execute_list:
        if 'name' in item:
            list_forms.append(item['name'])
    return list_forms


def construct_key_value_dictionaries(dictionary: dict[str, str],
                                     ) -> list[dict[str, str]]:
    """
    Составление из одного словаря, множество словарей
    вмещающие в себя `ключ - значение` каждого поля в
    единичном эземпляре

    Args:
        dictionary (dict[str, str]): словарь

    Returns:
        list[dict[str, str]]: список из словарей по ключу - значению
    """
    list_key_value = []
    for key, value in dictionary.items():
        list_key_value.append({key: value})
    return list_key_value
