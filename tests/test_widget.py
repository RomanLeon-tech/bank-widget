import pytest

from src.widget import get_date
from src.widget import mask_account_card


@pytest.mark.parametrize("input_string, expected", [
    ("Visa Platinum 7000792289606361", "7000 79** **** 6361"),
    ("Maestro 7000792289606361", "7000 79** **** 6361"),
    ("Счет 73654108430135874305", "**4305"),
])
def test_mask_account_card(input_string: str, expected: str) -> None:
    assert mask_account_card(input_string) == expected


@pytest.mark.parametrize("date_string, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-12-31T23:59:59.999999", "31.12.2023"),
])
def test_get_date(date_string: str, expected: str) -> None:
    assert get_date(date_string) == expected


def test_mask_account_card_invalid() -> None:
    with pytest.raises(ValueError):
        mask_account_card("Invalid input")


def test_get_date_invalid() -> None:
    with pytest.raises(ValueError):
        get_date("Invalid date")
