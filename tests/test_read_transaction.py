import csv
import os
from unittest.mock import Mock, patch

from src.read_transaction import read_csv, read_xlsx


def test_read_csv(capsys, test_read_csv_xlsx) -> None:
    mock_csv = Mock(return_value=test_read_csv_xlsx)
    csv.DictReader = mock_csv
    assert read_csv(os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")) == test_read_csv_xlsx
    read_csv("")
    message = capsys.readouterr()
    assert message.out == "[Errno 2] No such file or directory: ''\n"


@patch("pandas.read_excel")
def test_read_xlsx(mock_xlsx, test_read_xlsx_1, test_xlsx_result) -> None:
    mock_xlsx.return_value = test_read_xlsx_1
    assert (
        read_xlsx(os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")) == test_xlsx_result
    )


def test_read_xlsx_1():
    assert read_xlsx("") == []
