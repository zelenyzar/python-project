import json
import os
from unittest.mock import Mock, patch

from src.utils import currency_transaction, read_json


def test_read_json_1(test_read):
    mock_read = Mock(return_value=test_read)
    json.load = mock_read
    assert read_json(os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")) == test_read


def test_read_json_2(test_read):
    mock_read = Mock(return_value=test_read)
    json.load = mock_read
    assert read_json(os.path.join(os.path.dirname(__file__), "..", "data", "hjkhkj")) == []


def test_read_json_3(test_read_1):
    mock_read = Mock(return_value=test_read_1)
    json.load = mock_read
    assert read_json(os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")) == []


def test_read_json_4():
    mock_read = Mock(return_value=[])
    json.load = mock_read
    assert read_json(os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")) == []


@patch("src.utils.exchange_data")
def test_currency_transaction(mock_ex, test_read_3):
    mock_ex.return_value = 486.15
    assert currency_transaction(test_read_3) == 486.15


def test_currency_transaction_1(test_read_2):
    assert currency_transaction(test_read_2) == 31957.58
