from src.widget.masks import get_mask_card_number, get_mask_account

if __name__ == "__main__":
    card_number = 7000792289606361
    account_number = 73654108430135874305

    print(get_mask_card_number(card_number))  # 7000 79** **** 6361
    print(get_mask_account(account_number))  # **4305