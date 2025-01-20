import os
import requests
from typing import Union

def convert_currency(amount: float, from_currency: str, to_currency: str) -> Union[float, None]:
    """
    Конвертирует сумму из одной валюты в другую с использованием внешнего API.

    :param amount: Сумма для конвертации.
    :param from_currency: Исходная валюта.
    :param to_currency: Целевая валюта.
    :return: Конвертированная сумма или None в случае ошибки.
    """
    api_key = os.getenv("EXCHANGE_RATES_API_KEY")
    api_url = f"https://api.exchangeratesapi.io/latest?base={from_currency}&apikey={api_key}"
    response = requests.get(api_url)
    if response.status_code == 200:
        rates = response.json().get("rates", {})
        if to_currency in rates:
            return amount * rates[to_currency]
    return None
