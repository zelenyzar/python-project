from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(test_lists_5: list[dict[str, Any]], test_lists_6: list[dict[str, Any]]) -> None:
    assert next(filter_by_currency(test_lists_5, "USD")) == test_lists_6


def test_transaction_descriptions(test_lists_5: list[dict[str, Any]]) -> None:
    test_gen = transaction_descriptions(test_lists_5)
    assert next(test_gen) == "Перевод организации"
    assert next(test_gen) == "Перевод со счета на счет"


def test_card_number_generator_1() -> None:
    test_gen = card_number_generator(1, 5)
    assert next(test_gen) == "0000 0000 0000 0001"
    assert next(test_gen) == "0000 0000 0000 0002"


def test_card_number_generator_2() -> None:
    test_gen = card_number_generator(5, 1)
    assert next(test_gen) == "Начальное значение должно быть меньше конечного"


def test_card_number_generator_3() -> None:
    test_gen = card_number_generator(1, 2)
    next(test_gen)
    next(test_gen)
    with pytest.raises(StopIteration):
        next(test_gen)
