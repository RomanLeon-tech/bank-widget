import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from src.utils.file_reader import read_csv_file, read_excel_file


@pytest.fixture
def csv_file_path(tmp_path):
    file_path = tmp_path / "test_transactions.csv"
    data = [
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"}
    ]
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    return file_path


@pytest.fixture
def excel_file_path(tmp_path):
    file_path = tmp_path / "test_transactions.xlsx"
    data = [
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"}
    ]
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)
    return file_path


def test_read_csv_file(csv_file_path):
    expected = [
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"}
    ]
    result = read_csv_file(csv_file_path)
    assert result == expected


def test_read_excel_file(excel_file_path):
    expected = [
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"}
    ]
    result = read_excel_file(excel_file_path)
    assert result == expected


@patch("pandas.read_csv")
def test_read_csv_file_mock(mock_read_csv, tmp_path):
    mock_read_csv.return_value = pd.DataFrame([
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"}
    ])
    file_path = tmp_path / "test_transactions.csv"
    expected = [
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"}
    ]
    result = read_csv_file(file_path)
    assert result == expected


@patch("pandas.read_excel")
def test_read_excel_file_mock(mock_read_excel, tmp_path):
    mock_read_excel.return_value = pd.DataFrame([
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"}
    ])
    file_path = tmp_path / "test_transactions.xlsx"
    expected = [
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"}
    ]
    result = read_excel_file(file_path)
    assert result == expected
