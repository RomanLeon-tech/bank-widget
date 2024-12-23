from typing import Dict
from typing import List

import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date


@pytest.fixture
def operations() -> List[Dict[str, str]]:
    return [
        {'id': '41428829', 'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364'},
        {'id': '939719570', 'state': 'EXECUTED',
         'date': '2018-06-30T02:08:58.425572'},
        {'id': '594226727', 'state': 'CANCELED',
         'date': '2018-09-12T21:27:25.241689'},
        {'id': '615064591', 'state': 'CANCELED',
         'date': '2018-10-14T08:21:33.419441'}
    ]


def test_filter_by_state(operations: List[Dict[str, str]]) -> None:
    assert filter_by_state(operations, 'EXECUTED') == [
        {'id': '41428829', 'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364'},
        {'id': '939719570', 'state': 'EXECUTED',
         'date': '2018-06-30T02:08:58.425572'}
    ]
    assert filter_by_state(operations, 'CANCELED') == [
        {'id': '594226727', 'state': 'CANCELED',
         'date': '2018-09-12T21:27:25.241689'},
        {'id': '615064591', 'state': 'CANCELED',
         'date': '2018-10-14T08:21:33.419441'}
    ]


def test_sort_by_date(operations: List[Dict[str, str]]) -> None:
    assert sort_by_date(operations) == [
        {'id': '41428829', 'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364'},
        {'id': '615064591', 'state': 'CANCELED',
         'date': '2018-10-14T08:21:33.419441'},
        {'id': '594226727', 'state': 'CANCELED',
         'date': '2018-09-12T21:27:25.241689'},
        {'id': '939719570', 'state': 'EXECUTED',
         'date': '2018-06-30T02:08:58.425572'}
    ]
