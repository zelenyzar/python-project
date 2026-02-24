from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(number_card: str) -> str:
    """ Функция, которая принимает либо номер счета, либо номер карты """
    if "счет" in number_card.lower():
        return f"Счет {get_mask_account(number_card[-20:])}"
    else:
        return f"{number_card[:-17]} {get_mask_card_number(number_card[-16:])}"

def get_date(some_date: str) -> str:
    """ Функция, которая преобразовывает в формат ДД.ММ.ГГГГ """
    # 2024-03-11T02:26:18.671407
    date_a = some_date.split("T")
    date_b = date_a[0].split("-")
    return f"{date_b[2]}.{date_b[1]}.{date_b[0]}"