import pandas as pd
from typing import List, Dict, Any
from src.utils.logger import setup_logger

logger = setup_logger('file_reader', 'logs/file_reader.log')

def read_csv_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает CSV-файл и возвращает список словарей с данными о финансовых транзакциях.

    :param file_path: Путь к CSV-файлу.
    :return: Список словарей с данными о финансовых транзакциях.
    """
    try:
        df = pd.read_csv(file_path)
        data = df.to_dict(orient='records')
        logger.info(f"Successfully read CSV file: {file_path}")
        return data
    except Exception as e:
        logger.error(f"Error reading CSV file: {file_path}. {e}")
        return []

def read_excel_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает XLSX-файл и возвращает список словарей с данными о финансовых транзакциях.

    :param file_path: Путь к XLSX-файлу.
    :return: Список словарей с данными о финансовых транзакциях.
    """
    try:
        df = pd.read_excel(file_path)
        data = df.to_dict(orient='records')
        logger.info(f"Successfully read XLSX file: {file_path}")
        return data
    except Exception as e:
        logger.error(f"Error reading XLSX file: {file_path}. {e}")
        return []
