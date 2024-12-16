def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты по правилу XXXX XX** **** XXXX.

    :param card_number: Номер карты в виде числа.
    :return: Маска номера карты.
    """
    card_number_str = str(card_number)
    if len(card_number_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    return (
        f"{card_number_str[:4]} {card_number_str[4:6]}** **** "
        f"{card_number_str[-4:]}"
    )


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер счета по правилу **XXXX.

    :param account_number: Номер счета в виде числа.
    :return: Маска номера счета.
    """
    account_number_str = str(account_number)
    if len(account_number_str) != 20:
        raise ValueError("Номер счета должен содержать 20 цифр")

    return f"**{account_number_str[-4:]}"
