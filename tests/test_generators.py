# tests/test_generators.py

import pytest
from src.generators.transactions import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.mark.parametrize("transactions, currency, expected", [
    ([
        {"id": 1, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}}, "description": "Перевод организации", "from": "Счет 75106830613657916952", "to": "Счет 11776614605963066702"},
        {"id": 2, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878", "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}}, "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542", "to": "Счет 75651667383060284188"}
    ], "USD", [
        {"id": 1, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}}, "description": "Перевод организации", "from": "Счет 75106830613657916952", "to": "Счет 11776614605963066702"},
        {"id": 2, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878", "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}}, "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542", "to": "Счет 75651667383060284188"}
    ]),
    ([
        {"id": 3, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "operationAmount": {"amount": "9824.07", "currency": {"name": "RUB", "code": "RUB"}}, "description": "Перевод организации", "from": "Счет 75106830613657916952", "to": "Счет 11776614605963066702"},
        {"id": 4, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878", "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}}, "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542", "to": "Счет 75651667383060284188"}
    ], "RUB", [
        {"id": 3, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "operationAmount": {"amount": "9824.07", "currency": {"name": "RUB", "code": "RUB"}}, "description": "Перевод организации", "from": "Счет 75106830613657916952", "to": "Счет 11776614605963066702"},
        {"id": 4, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878", "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}}, "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542", "to": "Счет 75651667383060284188"}
    ])
])

def test_filter_by_currency(transactions, currency, expected):
    result = list(filter_by_currency(transactions, currency))
    assert result == expected

@pytest.mark.parametrize("transactions, expected", [
    ([
        {"id": 1, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}}, "description": "Перевод организации", "from": "Счет 75106830613657916952", "to": "Счет 11776614605963066702"},
        {"id": 2, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878", "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}}, "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542", "to": "Счет 75651667383060284188"}
    ], ["Перевод организации", "Перевод со счета на счет"]),
    ([
        {"id": 3, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "operationAmount": {"amount": "9824.07", "currency": {"name": "RUB", "code": "RUB"}}, "description": "Перевод организации", "from": "Счет 75106830613657916952", "to": "Счет 11776614605963066702"},
        {"id": 4, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878", "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}}, "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542", "to": "Счет 75651667383060284188"}
    ], ["Перевод организации", "Перевод со счета на счет"])
])

def test_transaction_descriptions(transactions, expected):
    result = list(transaction_descriptions(transactions))
    assert result == expected

@pytest.mark.parametrize("start, end, expected", [
    (1, 5, ["0000000000000001", "0000000000000002", "0000000000000003", "0000000000000004", "0000000000000005"]),
    (3, 7, ["0000000000000003", "0000000000000004", "0000000000000005", "0000000000000006", "0000000000000007"])
])

def test_card_number_generator(start, end, expected):
    result = list(card_number_generator(start, end,))
    assert result == expected
