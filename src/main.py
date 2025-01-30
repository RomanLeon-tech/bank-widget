import json
import csv
import pandas as pd
from typing import List, Dict
from src.utils.transaction_filter import filter_transactions_by_description
from src.utils.transaction_categorizer import categorize_transactions

def load_transactions_from_json(file_path: str) -> List[Dict[str, str]]:
    with open(file_path, 'r') as file:
        return json.load(file)

def load_transactions_from_csv(file_path: str) -> List[Dict[str, str]]:
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def load_transactions_from_excel(file_path: str) -> List[Dict[str, str]]:
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Введите номер пункта меню: ")
    if choice == '1':
        file_path = input("Введите путь к JSON-файлу: ")
        transactions = load_transactions_from_json(file_path)
    elif choice == '2':
        file_path = input("Введите путь к CSV-файлу: ")
        transactions = load_transactions_from_csv(file_path)
    elif choice == '3':
        file_path = input("Введите путь к XLSX-файлу: ")
        transactions = load_transactions_from_excel(file_path)
    else:
        print("Неверный выбор. Программа завершена.")
        return

    status = input("Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: ").upper()
    while status not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции \"{status}\" недоступен.")
        status = input("Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: ").upper()

    filtered_transactions = [t for t in transactions if t.get('state', '').upper() == status]
    print(f"Операции отфильтрованы по статусу \"{status}\"")

    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").lower()
    if sort_choice == 'да':
        sort_order = input("Отсортировать по возрастанию или по убыванию? ").lower()
        filtered_transactions.sort(key=lambda x: x.get('date', ''), reverse=(sort_order == 'по убыванию'))

    currency_choice = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if currency_choice == 'да':
        filtered_transactions = [t for t in filtered_transactions if t.get('operationAmount', {}).get('currency', {}).get('code', '') == 'RUB']

    search_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
    if search_choice == 'да':
        search_string = input("Введите слово для поиска: ")
        filtered_transactions = filter_transactions_by_description(filtered_transactions, search_string)

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
    for transaction in filtered_transactions:
        print(f"{transaction.get('date', '')} {transaction.get('description', '')}")
        print(f"Счет {transaction.get('from', '')} -> Счет {transaction.get('to', '')}")
        print(f"Сумма: {transaction.get('operationAmount', {}).get('amount', '')} {transaction.get('operationAmount', {}).get('currency', {}).get('code', '')}")
        print()

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")

if __name__ == "__main__":
    main()
