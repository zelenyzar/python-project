import json
from typing import Any

from src.external_api import exchange_data


def read_json(filename: str) -> list[dict[str:Any]]:
    """Функция чтения json-файла"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            transaction_list = json.load(f)
        if len(transaction_list) == 0:
            return []
        elif not isinstance(transaction_list, list):
            return []
        elif len(transaction_list) > 0:
            return transaction_list
    except FileNotFoundError:
        return []


def currency_transaction(transaction_given: dict[str:Any]) -> float:
    """Функция, принимающая транзакцию в любой валюте и возвращаюся сумму операции в рублях"""
    if transaction_given["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction_given["operationAmount"]["amount"])
    else:
        currency_code = transaction_given["operationAmount"]["currency"]["code"]
        currency_amount = float(transaction_given["operationAmount"]["amount"])
        result_sum = exchange_data(currency_code, currency_amount)
        return result_sum


# if __name__ == "__main__":
#     print(read_json("../data/operations.json"))
