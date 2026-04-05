import json
import logging
from typing import Any

from src.external_api import exchange_data

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
console_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
console_formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(lineno)d: %(message)s")
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)


def read_json(filename: str) -> list[dict[str:Any]]:
    """Функция чтения json-файла"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            transaction_list = json.load(f)
            logger.debug("Получены данные из файла")
        if len(transaction_list) == 0:
            logger.warning("Файл должен содержать данные")
            return []
        elif not isinstance(transaction_list, list):
            logger.warning("Файл не содержит список")
            return []
        elif len(transaction_list) > 0:
            logger.info("Получен список транзакций")
            return transaction_list
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
