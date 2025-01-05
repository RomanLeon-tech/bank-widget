import pytest
from src.generators.transactions import filter_by_currency, transaction_descriptions
from src.generators.cards import card_number_generator


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.206769",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    ]

def test_filter_by_currency():
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.206769",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    ]
    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions) == transactions[0]
    assert next(usd_transactions) == transactions[1]
    with pytest.raises(StopIteration):
        next(usd_transactions)

def test_transaction_descriptions():
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.206769",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    ]
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Открытие вклада"
    with pytest.raises(StopIteration):
        next(descriptions)

def test_card_number_generator():
    card_numbers = card_number_generator(1, 5)
    assert next(card_numbers) == "0000 0000 0000 0001"
    assert next(card_numbers) == "0000 0000 0000 0002"
    assert next(card_numbers) == "0000 0000 0000 0003"
    assert next(card_numbers) == "0000 0000 0000 0004"
    assert next(card_numbers) == "0000 0000 0000 0005"
    with pytest.raises(StopIteration):
        next(card_numbers)
