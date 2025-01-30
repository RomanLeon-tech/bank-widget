from src.utils.transaction_categorizer import categorize_transactions


def test_categorize_transactions():
    transactions = [
        {"description": "Transfer to account"},
        {"description": "Payment for services"},
        {"description": "Transfer from account"},
    ]
    categories = ["Transfer", "Payment"]
    expected = {
        "Transfer": 2,
        "Payment": 1,
    }
    result = categorize_transactions(transactions, categories)
    assert result == expected
