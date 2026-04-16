from typing import Any

import pandas as pd
import pytest


@pytest.fixture
def scheme_lists() -> str:
    return "73654108430135874305"


@pytest.fixture
def scheme_lists_2() -> str:
    return "736541084301358743050203405"


@pytest.fixture
def test_lists_3() -> list[dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def test_lists_4() -> list[dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def test_lists_5() -> list[dict[str, Any]]:
    return [
        {
            "amount": "16210",
            "currency_code": "RUB",
            "currency_name": "RUB",
            "date": "2023-09-05T11:30:32Z",
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "id": "650703",
            "state": "EXECUTED",
            "to": "Счет 39745660563456619397",
        },
        {
            "amount": "29740",
            "currency_code": "COP",
            "currency_name": "Peso",
            "date": "2020-12-06T23:00:58Z",
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "id": "3598919",
            "state": "EXECUTED",
            "to": "Discover 0720428384694643",
        },
    ]


@pytest.fixture
def test_lists_6() -> list[dict[str, Any]]:
    return {
        "amount": "16210",
        "currency_code": "RUB",
        "currency_name": "RUB",
        "date": "2023-09-05T11:30:32Z",
        "description": "Перевод организации",
        "from": "Счет 58803664561298323391",
        "id": "650703",
        "state": "EXECUTED",
        "to": "Счет 39745660563456619397",
    }


@pytest.fixture
def test_log():
    return "запуск my_function\nmy_function ok\n"


@pytest.fixture
def test_log_2():
    return (
        "запуск my_function\nmy_function error: "
        "TypeError unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2'), {}.\n"
    )


@pytest.fixture
def test_read():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]


@pytest.fixture
def test_test_read():
    return [
        {
            "amount": "31957.58",
            "currency_code": "RUB",
            "currency_name": "руб.",
            "date": "2019-08-26T10:50:58.294041",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "id": 441945886,
            "to": "Счет 64686473678894779589",
        },
        {
            "amount": "8221.37",
            "currency_code": "USD",
            "currency_name": "USD",
            "date": "2019-07-03T18:35:29.512364",
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "id": 41428829,
            "to": "Счет 35383033474447895560",
        },
    ]


@pytest.fixture
def test_read_1():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def test_read_2():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def test_read_3():
    return {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }


@pytest.fixture
def test_read_csv_xlsx():
    return [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]


@pytest.fixture
def test_read_xlsx_1():
    data = [
        ["24.04.2020", -2063, "RUB", "Супермаркеты", "Магнит"],
        ["19.03.2020", -2159, "RUB", "Супермаркеты", "Пятерочка"],
        ["06.04.2020", -2055, "RUB", "Супермаркеты", "Магнит"],
        ["14.05.2020", -507, "RUB", "Транспорт", "Такси"],
        ["21.03.2020", -607, "RUB", "Транспорт", "Такси"],
        ["07.02.2020", -3500, "RUB", "Перевод", "Иванов Д."],
        ["24.05.2020", -708, "RUB", "Переводы", "Лютикова Л."],
        ["13.03.2020", -1500, "RUB", "Наличные", "Снятие с банкомата"],
        ["06.05.2020", -2500, "RUB", "Наличные", "Снятие с банкомата"],
        ["11.04.2020", 1500, "RUB", "Бонусы", "КЭШбэк"],
        ["21.02.2020", 800, "RUB", "Бонусы", "КЭШбэк"],
    ]
    df = pd.DataFrame(data, columns=["Дата платежа", "Сумма операции", "Валюта операции", "Категория", "Описание"])
    return df


@pytest.fixture
def test_xlsx_result():
    return [
        {
            "Валюта операции": "RUB",
            "Дата платежа": "24.04.2020",
            "Категория": "Супермаркеты",
            "Описание": "Магнит",
            "Сумма операции": -2063,
        },
        {
            "Валюта операции": "RUB",
            "Дата платежа": "19.03.2020",
            "Категория": "Супермаркеты",
            "Описание": "Пятерочка",
            "Сумма операции": -2159,
        },
        {
            "Валюта операции": "RUB",
            "Дата платежа": "06.04.2020",
            "Категория": "Супермаркеты",
            "Описание": "Магнит",
            "Сумма операции": -2055,
        },
        {
            "Валюта операции": "RUB",
            "Дата платежа": "14.05.2020",
            "Категория": "Транспорт",
            "Описание": "Такси",
            "Сумма операции": -507,
        },
        {
            "Валюта операции": "RUB",
            "Дата платежа": "21.03.2020",
            "Категория": "Транспорт",
            "Описание": "Такси",
            "Сумма операции": -607,
        },
        {
            "Валюта операции": "RUB",
            "Дата платежа": "07.02.2020",
            "Категория": "Перевод",
            "Описание": "Иванов Д.",
            "Сумма операции": -3500,
        },
        {
            "Валюта операции": "RUB",
            "Дата платежа": "24.05.2020",
            "Категория": "Переводы",
            "Описание": "Лютикова Л.",
            "Сумма операции": -708,
        },
        {
            "Валюта операции": "RUB",
            "Дата платежа": "13.03.2020",
            "Категория": "Наличные",
            "Описание": "Снятие с банкомата",
            "Сумма операции": -1500,
        },
        {
            "Валюта операции": "RUB",
            "Дата платежа": "06.05.2020",
            "Категория": "Наличные",
            "Описание": "Снятие с банкомата",
            "Сумма операции": -2500,
        },
        {
            "Валюта операции": "RUB",
            "Дата платежа": "11.04.2020",
            "Категория": "Бонусы",
            "Описание": "КЭШбэк",
            "Сумма операции": 1500,
        },
        {
            "Валюта операции": "RUB",
            "Дата платежа": "21.02.2020",
            "Категория": "Бонусы",
            "Описание": "КЭШбэк",
            "Сумма операции": 800,
        },
    ]


@pytest.fixture
def test_search_word():
    return [
        {
            "amount": "16210",
            "currency_code": "PEN",
            "currency_name": "Sol",
            "date": "2023-09-05T11:30:32Z",
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "id": "650703",
            "state": "EXECUTED",
            "to": "Счет 39745660563456619397",
        },
        {
            "amount": "29740",
            "currency_code": "COP",
            "currency_name": "Peso",
            "date": "2020-12-06T23:00:58Z",
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "id": "3598919",
            "state": "EXECUTED",
            "to": "Discover 0720428384694643",
        },
    ]
