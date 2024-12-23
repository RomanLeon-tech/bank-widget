from typing import List, Dict, Optional
from datetime import datetime


def filter_by_state(operations: List[Dict[str, str]],
                    state: Optional[str] = "EXECUTED") -> List[Dict[str, str]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param operations: Список словарей с операциями.
    :param state: Значение для ключа 'state' (по умолчанию 'EXECUTED').
    :return: Новый список словарей, содержащий только те словари,
     у которых ключ 'state' соответствует указанному значению.
    """
    return [operation for operation in operations
            if operation.get("state") == state]


def sort_by_date(operations: List[Dict[str, str]],
                 reverse: bool = True) -> List[Dict[str, str]]:
    """
    Сортирует список словарей по дате.

    :param operations: Список словарей с операциями.
    :param reverse: Порядок сортировки (по умолчанию — убывание).
    :return: Новый список, отсортированный по дате.
    """
    return sorted(operations, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
