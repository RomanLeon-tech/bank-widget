from src.masks.logger import setup_logger

logger = setup_logger('mask_operations', 'logs/mask_operations.log')


def mask_card_number(card_number: str) -> str:
    """
<<<<<<< HEAD
    Маскирует номер карты, оставляя видимыми только
    первые 6 и последние 4 цифры.
=======
    Маскирует номер карты, оставляя
    видимыми только первые 6 и последние 4 цифры.
>>>>>>> develop

    :param card_number: Номер карты.
    :return: Маскированный номер карты.
    """
    try:
        if len(card_number) == 16:
            masked_number = card_number[:6] + '*' * 6 + card_number[-4:]
            logger.info(f"Successfully masked card number: {masked_number}")
            return masked_number
        else:
            logger.warning(f"Invalid card number length: {len(card_number)}")
            return card_number
    except Exception as e:
        logger.error(f"Error masking card number: {e}")
        return card_number


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счета, оставляя видимыми только последние 4 цифры.

    :param account_number: Номер счета.
    :return: Маскированный номер счета.
    """
    try:
        if account_number.startswith("Счет"):
            masked_number = ("Счет **" + '*' *
                             (len(account_number) - 10) + account_number[-4:])
            logger.info(f"Successfully masked account number: {masked_number}")
            return masked_number
        else:
            logger.warning(f"Invalid account number format: {account_number}")
            return account_number
    except Exception as e:
        logger.error(f"Error masking account number: {e}")
        return account_number
