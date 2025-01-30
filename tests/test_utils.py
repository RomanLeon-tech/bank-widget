import json

import pytest
from unittest.mock import patch, MagicMock
from src.utils.json_reader import read_json_file
from src.external_api.exchange_rates import convert_currency


@pytest.fixture
def json_file_path(tmp_path):
    return tmp_path / "test_operations.json"


@pytest.mark.parametrize("json_data, expected", [
    ([{"id": 1, "amount": 100, "currency": "USD"}],
     [{"id": 1, "amount": 100, "currency": "USD"}]),
    ([], []),
    (None, [])
])
def test_read_json_file(json_file_path, json_data, expected):
    if json_data is not None:
        with open(json_file_path, 'w') as file:
            json.dump(json_data, file)

    result = read_json_file(json_file_path)
    assert result == expected


@patch("src.external_api.exchange_rates.requests.get")
def test_convert_currency(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "conversion_rates": {
            "EUR": 0.85,
            "RUB": 75.0
        }
    }
    mock_get.return_value = mock_response

    assert convert_currency(100, "USD", "EUR") == 85.0
    assert convert_currency(100, "USD", "RUB") == 7500.0
    assert convert_currency(100, "USD", "JPY") is None
