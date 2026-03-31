from unittest.mock import patch

from src.external_api import exchange_data


@patch("requests.get")
def test_exchange_data_1(mock_get) -> None:
    mock_get.return_value.json.return_value = {"result": 200.2315}
    assert exchange_data(66.67, "EUR") == 200.23
