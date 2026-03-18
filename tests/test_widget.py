import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "number, expected",
    [
        ("Visa Platinum 1111111111111111", "Visa Platinum 1111 11** **** 1111"),
        ("Счет 22222222222222222222", "Счет **2222"),
    ],
)
def test_mask_account_card(number, expected):
    assert mask_account_card(number) == expected


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
