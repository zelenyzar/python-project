from typing import Any, Generator, Iterator


def filter_by_currency(transactions: list[dict[str, Any]], given_currency: str) -> Iterator:
    """Фунцкия, которая итератор, который поочередно возвращает транзакции с заданной валютой"""
    list_currency = []
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == given_currency:
            list_currency.append(transaction)
            yield list_currency


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Generator[Any, Any, None]:
    """Генератор, который принимает список словарей транзакции и возвращает описание операции"""
    for transaction in transactions:
        description = transaction["description"]
        yield description


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    if start < stop:
        for num in range(start, stop + 1):
            numbers = str(num).zfill(16)
            num_card = numbers[:4] + " " + numbers[4:8] + " " + numbers[8:12] + " " + numbers[12:]
            yield num_card
    else:
        yield "Начальное значение должно быть меньше конечного"
