import os
import requests
from typing import Union
from src.utils.logger import setup_logger

logger = setup_logger('exchange_rates', 'logs/exchange_rates.log')


<<<<<<< HEAD
def convert_currency(amount: float, from_currency: str, to_currency: str) -> (
        Union)[float, None]:
=======
def convert_currency(amount: float,
                     from_currency: str, to_currency: str) \
        -> Union[float, None]:
>>>>>>> develop
    """
    Конвертирует сумму из одной валюты в другую с
    использованием внешнего API.

    :param amount: Сумма для конвертации.
    :param from_currency: Исходная валюта.
    :param to_currency: Целевая валюта.
    :return: Конвертированная сумма или None в случае ошибки.
    """
    api_key = os.getenv("EXCHANGE_RATES_API_KEY")
<<<<<<< HEAD
    api_url = (f"https://v6.exchangerate-api.com/v6/{api_key}"
               f"/latest/{from_currency}")
=======
    api_url = (f"https://v6.exchangerate-api.com/v6/"
               f"{api_key}/latest/{from_currency}")
>>>>>>> develop
    response = requests.get(api_url)
    if response.status_code == 200:
        rates = response.json().get("conversion_rates", {})
        if to_currency in rates:
            logger.info(f"Successfully converted "
                        f"{amount} {from_currency} to {to_currency}")
            return amount * rates[to_currency]
        else:
            logger.warning(f"Conversion rate for {to_currency} not found")
    else:
        logger.error(f"Error fetching exchange rates: {response.status_code}")
    return None
