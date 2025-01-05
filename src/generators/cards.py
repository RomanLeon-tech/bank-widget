from typing import Generator


def card_number_generator(start: int, end: int) -> (
        Generator)[str, None, None]:
    """
    Генерирует номера банковских карт в заданном диапазоне.

    :param start: Начальное значение диапазона.
    :param end: Конечное значение диапазона.
    :return: Генератор, выдающий номера карт в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, end + 1):
        yield f"{number:016}"
