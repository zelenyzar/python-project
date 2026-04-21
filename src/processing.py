from typing import Any


def filter_by_state(list_dict: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция, которая фильтрует по статусу"""
    list_dict_new = []
    for dict_meaning in list_dict:
        if dict_meaning.get("state") == state:
            list_dict_new.append(dict_meaning)
    return list_dict_new


def sort_by_date(list_dict: list[dict[str, Any]], sort_option: bool = True) -> list[dict[str, Any]]:
    """Функция, которая сортирует список по дате в порядке убывания"""
    list_dict_new = sorted(list_dict, key=lambda k: k["date"], reverse=sort_option)
    return list_dict_new
