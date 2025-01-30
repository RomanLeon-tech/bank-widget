from src.utils.transaction_filter import filter_transactions_by_description


def test_filter_transactions_by_description():
    transactions = [
        {"description": "Transfer to account"},
        {"description": "Payment for services"},
        {"description": "Transfer from account"},
    ]
    search_string = "Transfer"
    expected = [
        {"description": "Transfer to account"},
        {"description": "Transfer from account"},
    ]
    result = filter_transactions_by_description(transactions, search_string)
    assert result == expected
