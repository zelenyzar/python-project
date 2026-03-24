import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

def test_filter_by_currency(test_lists_5, test_lists_6):
    assert next(filter_by_currency(test_lists_5, "USD")) == test_lists_6

def test_transaction_descriptions(test_lists_5):
    test_gen = transaction_descriptions(test_lists_5)
    assert next(test_gen) == "Перевод организации"
    assert next(test_gen) == "Перевод со счета на счет"

def test_card_number_generator_1():
    test_gen = card_number_generator(1,5)
    assert next(test_gen) == '0000 0000 0000 0001'
    assert next(test_gen) == '0000 0000 0000 0002'

def test_card_number_generator_2():
    test_gen = card_number_generator(5,1)
    assert next(test_gen) == 'Начальное значение должно быть меньше конечного'

def test_card_number_generator_3(capsys):
    test_gen = card_number_generator(1, 2)
    next(test_gen)
    next(test_gen)
    with pytest.raises(StopIteration):
        next(test_gen)
