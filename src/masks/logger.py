import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str, log_file: str, level: int = logging.DEBUG) -> logging.Logger:
    """
    Настраивает логгер для модуля.

    :param name: Имя логгера.
    :param log_file: Путь к файлу лога.
    :param level: Уровень логирования.
    :return: Настроенный логгер.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Создаем обработчик для записи логов в файл
    file_handler = RotatingFileHandler(log_file, maxBytes=10**6, backupCount=5)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    # Добавляем обработчик к логгеру
    logger.addHandler(file_handler)

    return logger
