import pytest
from src.masks.mask_operations import mask_card_number, mask_account_number


@pytest.mark.parametrize("card_number, expected", [
    ("1234567890123456", "123456******3456"),
    ("1234567890", "1234567890"),
    ("", "")
])
def test_mask_card_number(card_number, expected):
    assert mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [
    ("Счет12345678901234567890", "Счет **34567890"),
    ("Счет1234567890", "Счет1234567890"),
    ("", "")
])
def test_mask_account_number(account_number, expected):
    assert mask_account_number(account_number) == expected
