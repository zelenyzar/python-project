from typing import Union


def get_mask_card_number(numbers_card: Union[str]) -> Union[str]:
    """Функция, маскирующая номер карты"""
    new_numbers_card = []
    for num in range(len(numbers_card)):
        if 6 <= num <= 11:
            new_numbers_card.append("*")
        else:
            new_numbers_card.append(numbers_card[num])
    new_numbers_card.insert(4, " ")
    new_numbers_card.insert(9, " ")
    new_numbers_card.insert(14, " ")
    result_numbers_card = "".join(new_numbers_card)
    return result_numbers_card


def get_mask_account(numbers_account: Union[str]) -> Union[str]:
    """Функция, маскирующая номер карты"""
    new_numbers_account = []
    for num in range(len(numbers_account)):
        if 14 <= num <= 15:
            new_numbers_account.append("*")
        elif 16 <= num:
            new_numbers_account.append(numbers_account[num])
    result_numbers_account = "".join(new_numbers_account)
    return result_numbers_account
