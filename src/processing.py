from typing import Any


def filter_by_state(list_dict: list[dict[str: Any]], state: str = "EXECUTED") -> list[dict[str: Any]]:
    """Функция, которая фильтрует по статусу"""
    list_dict_new = []
    for dict_meaning in list_dict:
        if dict_meaning["state"] == state:
            list_dict_new.append(dict_meaning)
    return list_dict_new




# if __name__ == '__main__':
#     result_dict = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
#     print(filter_by_state(result_dict))
#     print(sort_by_date(result_dict))