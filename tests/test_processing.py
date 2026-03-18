from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(test_lists_3):
    assert filter_by_state(test_lists_3) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date(test_lists_3, test_lists_4):
    assert sort_by_date(test_lists_3) == test_lists_4
