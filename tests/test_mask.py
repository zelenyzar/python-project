import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_account(scheme_lists: str) -> None:
    assert get_mask_account(scheme_lists) == "**4305"


@pytest.mark.parametrize(
    "number_card, expected",
    [("1111111111111111", "1111 11** **** 1111"), ("2222222222222222", "2222 22** **** 2222")],
)
def test_get_mask_card_number(number_card: str, expected: str) -> None:
    assert get_mask_card_number(number_card) == expected
