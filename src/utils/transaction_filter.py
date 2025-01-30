import re
from typing import List, Dict


def filter_transactions_by_description(transactions: List[Dict[str, str]],
                                       search_string: str) -> \
        (List)[Dict[str, str]]:

                                       search_string: str) -> (List)[Dict[str, str]]:
    """
    Фильтрует транзакции по строке поиска в описании.

    :param transactions: Список словарей с данными о банковских операциях.
    :param search_string: Строка поиска.
    :return: Список словарей, у которых в описании есть данная строка.
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [transaction for transaction in
            transactions if pattern.search
            (transaction.get('description', ''))]
    return [transaction for transaction in transactions
            if pattern.search(transaction.get('description', ''))]
