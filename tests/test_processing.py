import pytest

import main
from src.processing import list_date_sort, list_dict_sort


@pytest.fixture
def state_list_dict_test() -> (
    list[list[dict[str, str | int] | dict[str, str | int] | dict[str, str | int] | dict[str, str | int]]]
):
    """
        Возвращает тестовый список словарей
        :return: list[list[dict[str, str | int] | dict[str, str | int] | dict[str, str | int] | dict[str, str | int]]]
    )
    """
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
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
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
    [
        (
            main.state_list_dict,
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        )
    ],
)
def test_list_dict_sort_2(state_list_dict_test: list[dict], expected: str) -> None:
    assert list_dict_sort(state_list_dict_test, "CANCELED") == expected


@pytest.mark.parametrize(
    "list_date_sort_test, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )
    ],
)
def test_list_date_sort(list_date_sort_test: list[dict], expected: list[dict]) -> None:
    assert list_date_sort(list_date_sort_test, True) == expected
    assert list_date_sort(list_date_sort_test, False) == expected[::-1]
