import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, transactions


@pytest.fixture
def transactions_test() -> list[dict]:
    """
    Возвращает список словарей для тестов
    :return: list[dict]
    """
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_filter_by_currency(transactions_test: list[dict]) -> None:
    """
    Тест для вывода id по code
    :param transactions_test: list[dict]
    :return: None
    """
    usd_transactions = list(filter_by_currency(transactions, "USD")) == [939719570, 142264268, 895315941]
    for _ in range(usd_transactions):
        assert 939719570
        assert 142264268
        assert 895315941

    rub_transactions = list(filter_by_currency(transactions, "RUB")) == [873106923, 594226727]
    for _ in range(rub_transactions):
        assert 873106923
        assert 594226727


def test_transaction_descriptions(transactions_test: list[dict]) -> None:
    """
    Функция вывода операций из списка
    :param transactions_test: list[dict]
    :return: None
    """
    descriptions = list(transaction_descriptions(transactions)) == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    for _ in range(descriptions):
        assert "Перевод организации"
        assert "Перевод со счета на счет"
        assert "Перевод со счета на счет"
        assert "Перевод с карты на карту"
        assert "Перевод организации"


def test_card_number_generator() -> None:
    """
    Тест проверки генерации номеров карт
    :return: None
    """
    for card_number in card_number_generator(9991, 9999):
        card_test = list(card_number) == [
            "0000 0000 0000 9991",
            "0000 0000 0000 9992",
            "0000 0000 0000 9993",
            "0000 0000 0000 9994",
            "0000 0000 0000 9995",
            "0000 0000 0000 9996",
            "0000 0000 0000 9997",
            "0000 0000 0000 9998",
            "0000 0000 0000 9999",
        ]
        for _ in range(card_test):
            assert card_test
