import pytest

from src.widget import card_full_printer, date_optimizer


@pytest.fixture
def date_for_date() -> list[str]:
    """
    Возвращает список из 1 строки для тестов
    :return: list[str]
    """
    return ["2018-07-11T02:26:18.671407"]


@pytest.mark.parametrize("date_for_date, expected", [("2018-07-11T02:26:18.671407", "11.07.2018")])
def test_date_optimizer(date_for_date: str, expected: str) -> None:
    assert date_optimizer(date_for_date) == expected


@pytest.fixture
def arg_test() -> list:
    """
    Тестовый список карт для проверки
    :return: list
    """
    return [
        "Maestro 1596837868705199",
        "MasterCard 7158300734726758",
        "Счет 64686473678894779589",
        "Счет 35383033474447895560",
    ]


@pytest.mark.parametrize(
    "arg_test, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_card_full_printer(arg_test: str, expected: str) -> None:
    assert card_full_printer(arg_test) == expected
