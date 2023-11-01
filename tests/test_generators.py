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
    usd_transactions = filter_by_currency(transactions, "USD")

    for _ in range(1):
        assert next(usd_transactions)["id"] == 939719570
    for _ in range(1, 2):
        assert next(usd_transactions)["id"] == 142264268
    for _ in range(0, 1):
        assert next(usd_transactions)["id"] == 895315941

    rub_transactions = filter_by_currency(transactions, "RUB")

    for _ in range(1):
        assert next(rub_transactions)["id"] == 873106923
    for _ in range(1, 2):
        assert next(rub_transactions)["id"] == 594226727


def test_transaction_descriptions(transactions_test: list[dict]) -> None:
    descriptions = transaction_descriptions(transactions)
    for _ in range(1):
        assert next(descriptions) == "Перевод организации"
    for _ in range(2, 3):
        assert next(descriptions) == "Перевод со счета на счет"
    for _ in range(3, 4):
        assert next(descriptions) == "Перевод со счета на счет"
    for _ in range(4, 5):
        assert next(descriptions) == "Перевод с карты на карту"
    for _ in range(5, 6):
        assert next(descriptions) == "Перевод организации"


def test_card_number_generator() -> None:
    for card_number in card_number_generator(0, 0):
        assert card_number == "0000 0000 0000 0000"
    for card_number in card_number_generator(1000, 1000):
        assert card_number == "0000 0000 0000 1000"
    for card_number in card_number_generator(9999, 9999):
        assert card_number == "0000 0000 0000 9999"
