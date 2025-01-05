from typing import List, Dict, Generator


def filter_by_currency(transactions: List[Dict],
                       currency: str) -> Generator[Dict, None, None]:
    """
    Фильтрует транзакции по заданной валюте.

    :param transactions: Список словарей с транзакциями.
    :param currency: Валюта для фильтрации.
    :return: Генератор, выдающий транзакции с заданной валютой.
    """
    for transaction in transactions:
        if transaction['operationAmount']['currency']['name'] == currency:
            yield transaction

def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    """
    Возвращает описание каждой транзакции по очереди.

    :param transactions: Список словарей с транзакциями.
    :return: Генератор, выдающий описания транзакций.
    """
    for transaction in transactions:
        yield transaction['description']
