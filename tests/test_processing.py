import pytest

from src.processing import list_dict_sort, list_date_sort, sum_divisible_by_3_or_5, check


@pytest.fixture
def state_list_dict_test():
    return [[
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]]


def list_date_sort_test():
    return [[
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]]


def list_date_sort_test_2():
    return [[
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]]


def lst_test():
    return [[0], [1, 4, 7], [1, 2, 3, 4, 5]]


def email_test():
    return ['', 'choobaiz@sveta.net', 'choobaizsvetanet', '123', "@@@@@", "@.@.@.@.@"]


@pytest.mark.parametrize("state_list_dict_test, expected", [([
                                                                 {'id': 41428829, 'state': 'EXECUTED',
                                                                  'date': '2019-07-03T18:35:29.512364'},
                                                                 {'id': 939719570, 'state': 'EXECUTED',
                                                                  'date': '2018-06-30T02:08:58.425572'},
                                                                 {'id': 594226727, 'state': 'CANCELED',
                                                                  'date': '2018-09-12T21:27:25.241689'},
                                                                 {'id': 615064591, 'state': 'CANCELED',
                                                                  'date': '2018-10-14T08:21:33.419441'}
                                                             ], [{'id': 41428829, 'state': 'EXECUTED',
                                                                  'date': '2019-07-03T18:35:29.512364'},
                                                                 {'id': 939719570, 'state': 'EXECUTED',
                                                                  'date': '2018-06-30T02:08:58.425572'}])])
def test_list_dict_sort(state_list_dict_test: list[dict], expected):
    assert list_dict_sort(state_list_dict_test, "EXECUTED") == expected


@pytest.mark.parametrize("state_list_dict_test, expected", [([
                                                                 {'id': 41428829, 'state': 'EXECUTED',
                                                                  'date': '2019-07-03T18:35:29.512364'},
                                                                 {'id': 939719570, 'state': 'EXECUTED',
                                                                  'date': '2018-06-30T02:08:58.425572'},
                                                                 {'id': 594226727, 'state': 'CANCELED',
                                                                  'date': '2018-09-12T21:27:25.241689'},
                                                                 {'id': 615064591, 'state': 'CANCELED',
                                                                  'date': '2018-10-14T08:21:33.419441'}
                                                             ], [{'id': 594226727, 'state': 'CANCELED',
                                                                  'date': '2018-09-12T21:27:25.241689'},
                                                                 {'id': 615064591, 'state': 'CANCELED',
                                                                  'date': '2018-10-14T08:21:33.419441'}])])
def test_list_dict_sort_2(state_list_dict_test: list[dict], expected):
    assert list_dict_sort(state_list_dict_test, "CANCELED") == expected


@pytest.mark.parametrize("list_date_sort_test, expected", [([
                                                                {'id': 41428829, 'state': 'EXECUTED',
                                                                 'date': '2019-07-03T18:35:29.512364'},
                                                                {'id': 939719570, 'state': 'EXECUTED',
                                                                 'date': '2018-06-30T02:08:58.425572'},
                                                                {'id': 594226727, 'state': 'CANCELED',
                                                                 'date': '2018-09-12T21:27:25.241689'},
                                                                {'id': 615064591, 'state': 'CANCELED',
                                                                 'date': '2018-10-14T08:21:33.419441'}
                                                            ], [{'id': 41428829, 'state': 'EXECUTED',
                                                                 'date': '2019-07-03T18:35:29.512364'},
                                                                {'id': 615064591, 'state': 'CANCELED',
                                                                 'date': '2018-10-14T08:21:33.419441'},
                                                                {'id': 594226727, 'state': 'CANCELED',
                                                                 'date': '2018-09-12T21:27:25.241689'},
                                                                {'id': 939719570, 'state': 'EXECUTED',
                                                                 'date': '2018-06-30T02:08:58.425572'}])])
def test_list_dict_sort(list_date_sort_test: list[dict], expected):
    assert list_date_sort(list_date_sort_test, True) == expected


@pytest.mark.parametrize("list_date_sort_test_2, expected", [([
                                                                  {'id': 41428829, 'state': 'EXECUTED',
                                                                   'date': '2019-07-03T18:35:29.512364'},
                                                                  {'id': 939719570, 'state': 'EXECUTED',
                                                                   'date': '2018-06-30T02:08:58.425572'},
                                                                  {'id': 594226727, 'state': 'CANCELED',
                                                                   'date': '2018-09-12T21:27:25.241689'},
                                                                  {'id': 615064591, 'state': 'CANCELED',
                                                                   'date': '2018-10-14T08:21:33.419441'}
                                                              ], [{'id': 939719570, 'state': 'EXECUTED',
                                                                   'date': '2018-06-30T02:08:58.425572'},
                                                                  {'id': 594226727, 'state': 'CANCELED',
                                                                   'date': '2018-09-12T21:27:25.241689'},
                                                                  {'id': 615064591, 'state': 'CANCELED',
                                                                   'date': '2018-10-14T08:21:33.419441'},
                                                                  {'id': 41428829, 'state': 'EXECUTED',
                                                                   'date': '2019-07-03T18:35:29.512364'}])])
def test_list_dict_sort_2(list_date_sort_test_2: list[dict], expected):
    assert list_date_sort(list_date_sort_test_2, False) == expected


@pytest.mark.parametrize("lst_test, expected", [([0], 0), ([1, 4, 7], 0), ([1, 2, 3, 4, 5], 8)])
def test_sum_divisible_by_3_or_5(lst_test: list, expected):
    assert sum_divisible_by_3_or_5(lst_test) == expected


@pytest.mark.parametrize("email_test, expected", [('', "Неверный Email"), ('choobaiz@sveta.net', "Верный Email"),
                                                  ('choobaizsvetanet', "Неверный Email"), ('123', "Неверный Email"),
                                                  ("@@@@@", "Неверный Email"), ("@.@.@.@.@", "Неверный Email"), ])
def test_email(email_test: list, expected):
    assert check(email_test) == expected
