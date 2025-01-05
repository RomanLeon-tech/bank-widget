import logging
from functools import wraps
from typing import Callable, Any, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования выполнения функции.

    :param filename: Имя файла для записи логов. Если не указано, логи выводятся в консоль.
    :return: Декоратор.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)
            if filename:
                handler = logging.FileHandler(filename)
            else:
                handler = logging.StreamHandler()
            formatter = logging.Formatter('%(name)s %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)

            try:
                result = func(*args, **kwargs)
                logger.info(f"ok")
                return result
            except Exception as e:
                logger.error(f"error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise
            finally:
                logger.removeHandler(handler)

        return wrapper

    return decorator
