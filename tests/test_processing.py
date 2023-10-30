import pytest

import main
from src.processing import check_email, list_dict_sort, sum_divisible_by_3_or_5


@pytest.fixture
def state_list_dict_test() -> (
        list[list[dict[str, str | int] | dict[str, str | int] | dict[str, str | int] | dict[str, str | int]]]
):
    return [
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    ]


def email_test() -> list[str]:
    return ["", "choobaiz@sveta.net", "choobaizsvetanet", "123", "@@@@@", "@.@.@.@.@"]


@pytest.mark.parametrize(
    "list_date_sort_test, expected",
    [
        (
                main.state_list_dict,
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                ],
        )
    ],
)
def test_list_dict_sort(list_date_sort_test: list[dict], expected: list[dict]) -> None:
    assert list_dict_sort(list_date_sort_test, "EXECUTED") == expected


@pytest.mark.parametrize(
    "state_list_dict_test, expected",
    [(main.state_list_dict, [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])],
)
def test_list_dict_sort_2(state_list_dict_test: list[dict], expected: str) -> None:
    assert list_dict_sort(state_list_dict_test, "CANCELED") == expected


@pytest.fixture
def list_date_sort_test() -> (
        list[list[dict[str, str | int] | dict[str, str | int] | dict[str, str | int] | dict[str, str | int]]]
):
    return [
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    ]


@pytest.mark.parametrize(
    "list_date_sort_test, expected",
    [
        (
                list_date_sort_test,
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                ],
        )
    ],
)
@pytest.fixture
def lst_test() -> list[list[int]]:
    return [[0], [1, 4, 7], [1, 2, 3, 4, 5]]


@pytest.mark.parametrize("lst_test, expected", [([0], 0), ([1, 4, 7], 0), ([1, 2, 3, 4, 5], 8)])
def test_sum_divisible_by_3_or_5(lst_test: list, expected: str) -> None:
    assert sum_divisible_by_3_or_5(lst_test) == expected


@pytest.mark.parametrize(
    "email, expected",
    [
        ("", "Неверный Email"),
        ("choobaiz@sveta.net", "Верный Email"),
        ("choobaizsvetanet", "Неверный Email"),
        ("123", "Неверный Email"),
        ("@@@@@", "Неверный Email"),
        ("@.@.@.@.@", "Неверный Email"),
    ],
)
def test_check_email(email: str, expected: str) -> None:
    assert check_email(email) == expected
