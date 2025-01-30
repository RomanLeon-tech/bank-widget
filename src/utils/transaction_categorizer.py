from typing import List, Dict
from collections import Counter
from collections import defaultdict


def categorize_transactions(transactions: List[Dict[str, str]],
                            categories: List[str]) \
        -> Dict[str, int]:

                            categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций в каждой категории.

    :param transactions: Список словарей с данными о банковских операциях.
    :param categories: Список категорий операций.
    :return: Словарь, в котором ключи —
    это названия категорий, а значения — это
    количество операций в каждой категории.
    :return: Словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """
    category_count = Counter()
    category_count = defaultdict(int)
    for transaction in transactions:
        description = transaction.get('description', '')
        for category in categories:
            if category.lower() in description.lower():
                category_count[category] += 1
    return dict(category_count)
