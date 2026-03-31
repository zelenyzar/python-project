import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")


def exchange_data(amount_given: int | float, currency_given: str) -> float:
    """API запрос, конвертация в рубли"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_given}&amount={amount_given}"

    payload = {}

    headers = {"apikey": os.getenv("API_KEY")}

    response = requests.get(url, headers=headers, data=payload)
    result = response.json().get("result")
    return round(result, 2)
    # status_code = response.status_code
    # return response.json()
    # , status_code)


if __name__ == "__main__":
    print(exchange_data(1, "USD"))

    # result = response.json().get('result')
