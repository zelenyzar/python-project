import os

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_transaction import read_csv, read_xlsx
from src.utils import read_json, search_word
from src.widget import get_date, mask_account_card

BASE_DIR = os.path.dirname(__file__)
path_file = {
    "1": BASE_DIR + "/data/operations.json",
    "2": BASE_DIR + "/data/transactions.csv",
    "3": BASE_DIR + "/data/transactions_excel.xlsx",
}

read_file = {"1": read_json, "2": read_csv, "3": read_xlsx}

message_file = {
    "1": "Для обработки выбран JSON-файл",
    "2": "Для обработки выбран CSV-файл",
    "3": "Для обработки выбран XLSX-файл",
}

operation_status = ["EXECUTED", "CANCELED", "PENDING"]


def main():
    while True:
        quest_1 = input(
            "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла\n"
        )
        if quest_1 in ["1", "2", "3"]:
            read_func = read_file.get(quest_1)
            if read_func:
                print(message_file.get(quest_1))
                path = path_file.get(quest_1)
                transaction = read_func(path)
                break
    while True:
        quest_2 = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        ).upper()
        if quest_2 in operation_status:
            transaction = filter_by_state(transaction, quest_2)
            print(f"Операции отфильтрованы по статусу: {quest_2}")
            break
        else:
            print(f"Статус операции {quest_2} недоступен")
    quest_3_1 = input("Отсортировать операции по дате? Да/Нет \n").lower()
    if quest_3_1 == "да":
        quest_3_2 = input("Отсортировать по возрастанию или по убыванию? По возрастанию/По убыванию \n").lower()
        if quest_3_2 == "по убыванию":
            transaction = sort_by_date(transaction)
        elif quest_3_2 == "по возрастанию":
            transaction = sort_by_date(transaction, False)
        else:
            print("Параметр задан неверно. Сортировка произведена автоматически - по убыванию")
            transaction = sort_by_date(transaction)
    quest_4 = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
    if quest_4 == "да":
        transaction = list(filter_by_currency(transaction, "RUB"))
    quest_5 = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет \n").lower()
    if quest_5 == "да":
        quest_5_1 = input("Введите слово для фильтрации\n").lower()
        transaction = search_word(transaction, quest_5_1)
    if len(transaction) == 0:
        print("Транзакции не найдены")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(transaction)}")
        for i in transaction:
            print(i)
            date_inf = get_date(i.get("date"))
            description_inf = i.get("description")
            oper_from = i.get("from", "")
            oper_to = mask_account_card(i.get("to", ""))
            amount_inf = i.get("amount")
            inf_1 = f"{date_inf} {description_inf}"
            inf_2 = mask_account_card(oper_from) if oper_from else "" + "->"
            inf_3 = f"{oper_to}"
            inf_4 = f'Сумма: {amount_inf} {i.get("currency_name")}'
            print(f"{inf_1}\n{inf_2} {inf_3}\n{inf_4}\n\n")


if __name__ == "__main__":
    main()
