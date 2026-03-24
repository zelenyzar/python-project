from typing import Any, Iterator, Generator


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


if __name__ == "__main__":
    currency_list = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
    ]
    # cc = card_number_generator(9,13)
    # print(next(cc))
    # print(next(cc))
    # print(next(cc))
    # print(next(card_number_generator(9, 11)))
    # print(next(filter_by_currency(currency_list, "USD")))
    # print(next(transaction_descriptions(currency_list)))
    # # print(next(transaction_descriptions(filter_by_currency(currency_list, "USD"))))
    # print(next(transaction_descriptions(currency_list)))
    # print(next(transaction_descriptions(currency_list)))
    # aa = transaction_descriptions(currency_list)
    # bb = filter_by_currency(currency_list, given_currency="USD")
    # print(next(bb))
    # print(next(bb))
    # print(next(aa))
    # print(next(aa))
