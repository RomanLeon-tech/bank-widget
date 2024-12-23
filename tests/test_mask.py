import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


@pytest.mark.parametrize("card_number, expected", [
    (7000792289606361, "7000 79** **** 6361"),
    (1234567890123456, "1234 56** **** 3456"),
])
def test_get_mask_card_number(card_number: int, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [
    (73654108430135874305, "**4305"),
    (12345678901234567890, "**7890"),
])
def test_get_mask_account(account_number: int, expected: str) -> None:
    assert get_mask_account(account_number) == expected


def test_get_mask_card_number_invalid() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(123456)


def test_get_mask_account_invalid() -> None:
    with pytest.raises(ValueError):
        get_mask_account(1234567890)
