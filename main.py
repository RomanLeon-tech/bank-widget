from src.widget import mask_account_card, get_date

if __name__ == "__main__":
    # Примеры для тестирования функции mask_account_card
    print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361
    print(mask_account_card("Maestro 7000792289606361"))  # Maestro 7000 79** **** 6361
    print(mask_account_card("Счет 73654108430135874305"))  # Счет **4305

    # Примеры для тестирования функции get_date
    print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024
