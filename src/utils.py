import json
import logging
import os
import re
from collections import Counter
from typing import Any

from src.external_api import exchange_data

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
path_name = os.path.join(os.path.dirname(__file__), "..", "logs", "utils.log")
console_handler = logging.FileHandler(path_name, mode="w", encoding="utf-8")
console_formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(lineno)d: %(message)s")
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)


def read_json(filename: str) -> list[dict[str:Any]]:
    """Функция чтения json-файла"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            transaction_list = json.load(f)
            logger.debug("Получены данные из файла")
        new_transaction_list = []
        if len(transaction_list) == 0:
            logger.warning("Файл должен содержать данные")
            return []
        elif not isinstance(transaction_list, list):
            logger.warning("Файл не содержит список")
            return []
        for transaction in transaction_list:
            amount = transaction.get("operationAmount", {}).get("amount")
            currency_name = transaction.get("operationAmount", {}).get("currency", {}).get("name")
            currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
            new_transaction_list.append(
                {
                    "id": transaction.get("id"),
                    "state": transaction.get("state"),
                    "date": transaction.get("date"),
                    "amount": amount,
                    "currency_code": currency_code,
                    "currency_name": currency_name,
                    "from": transaction.get("from"),
                    "to": transaction.get("to"),
                    "description": transaction.get("description"),
                }
            )
        if len(new_transaction_list) > 0:
            logger.info("Получен список транзакций")
            return new_transaction_list
    except FileNotFoundError as e:
        logger.error(f"Произошла ошибка: {e}")
        return []


def currency_transaction(transaction_given: dict[str:Any]) -> float:
    """Функция, принимающая транзакцию в любой валюте и возвращаюся сумму операции в рублях"""
    if transaction_given["operationAmount"]["currency"]["code"] == "RUB":
        logger.info("Получена сумма в рублях")
        return float(transaction_given["operationAmount"]["amount"])
    else:
        currency_code = transaction_given["operationAmount"]["currency"]["code"]
        currency_amount = float(transaction_given["operationAmount"]["amount"])
        result_sum = exchange_data(currency_code, currency_amount)
        logger.info("Сумма конвертирована в рубли")
        return result_sum


def search_word(transaction_list: list[dict[str:Any]], key_word: str) -> list[dict[str:Any]]:
    """Поиск транзакций по ключевому слову"""
    result_list = []
    if key_word == "" or key_word == " ":
        print("Вы не задали слово")
    else:
        pattern = re.compile(rf"{key_word}", re.IGNORECASE)
        for transaction in transaction_list:
            if pattern.search(transaction.get("description", "")):
                result_list.append(transaction)
        if len(result_list) == 0:
            print("Операции не найдены")
    return result_list


def filter_state(transaction_list: list[dict[str:Any]]) -> dict[str : int | float]:
    """Функция фильтрации по статусу"""
    result_list = dict(Counter([i["state"] for i in transaction_list]))
    return result_list
