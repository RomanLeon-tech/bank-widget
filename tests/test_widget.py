import pytest

from src.widget import get_date
from src.widget import mask_account_number


@pytest.mark.parametrize("input_string, expected", [
    ("Visa Platinum 7000792289606361", "7000 79** **** 6361"),
    ("Maestro 7000792289606361", "7000 79** **** 6361"),
    ("Счет 73654108430135874305", "**4305"),
])
def test_mask_account_number(input_string: str, expected: str) -> None:
    assert mask_account_number(input_string) == expected


@pytest.mark.parametrize("date_str, expected", [
    ("2023-10-01T12:34:56", "2023-10-01"),
    ("2023-10-01T12:34:56.789", "2023-10-01"),
    ("", "")
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected


def test_mask_account_number_invalid() -> None:
    with pytest.raises(ValueError):
        mask_account_number("Invalid input")


def test_get_date_invalid() -> None:
    with pytest.raises(ValueError):
        get_date("Invalid date")
