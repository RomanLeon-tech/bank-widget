import json
from typing import List, Dict, Any
from src.utils.logger import setup_logger

logger = setup_logger('json_reader', 'logs/json_reader.log')


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей с
    данными о финансовых транзакциях.

    :param file_path: Путь к JSON-файлу.
    :return: Список словарей с данными о финансовых транзакциях.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Successfully read JSON file: {file_path}")
                return data
            else:
                logger.warning(f"JSON file does not contain a list:"
                               f" {file_path}")
                return []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error reading JSON file: {file_path}. {e}")
        return []
