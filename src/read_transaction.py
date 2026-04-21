import csv
from typing import Any

import pandas as pd


def read_csv(filename: str) -> list[dict[str:Any]]:
    """Функция чтения csv-файла"""
    list_transactions = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            for row in reader:
                list_transactions.append(row)
    except FileNotFoundError as e:
        print(e)
    return list_transactions


def read_xlsx(filename: str) -> list[dict[str:Any]]:
    """Функция чтения exсel-файла"""
    try:
        df_transactions = pd.read_excel(filename)
        df_transactions = df_transactions.fillna("")
        dict_transactions = df_transactions.to_dict(orient="records")
        return dict_transactions
    except FileNotFoundError:
        return []
