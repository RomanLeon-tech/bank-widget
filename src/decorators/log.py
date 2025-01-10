import logging
from functools import wraps
from typing import Callable, Any, Optional

def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования выполнения функции.

    :param filename: Имя файла для записи логов.
    Если не указано, логи выводятся в консоль.
    :return: Декоратор.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            global file_handler
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)

            if filename:
                file_handler = logging.FileHandler(filename)
                file_handler.setFormatter(logging.Formatter('%(name)s %(message)s'))
                logger.addHandler(file_handler)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter('%(name)s %(message)s'))
            logger.addHandler(console_handler)

            try:
                result = func(*args, **kwargs)
                logger.info("ok")
                return result
            except Exception as e:
                logger.error(f"error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise
            finally:
                if filename:
                    logger.removeHandler(file_handler)
                logger.removeHandler(console_handler)

        return wrapper

    return decorator
