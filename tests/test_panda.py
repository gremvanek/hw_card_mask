import pathlib
from typing import Any

from src.panda import universal_opener
import pytest

ROOT_PATH = pathlib.Path(__file__).parent.parent
FILE_PATH_CSV = ROOT_PATH.joinpath("data_files", "transactions_2.csv")
FILE_PATH_XLSX = ROOT_PATH.joinpath("data_files", "transactions_excel.xlsx")
FILE_PATH_JSON = ROOT_PATH.joinpath("data_files", "operations.json")


@pytest.fixture
def transaction_tests() -> Any:
    sample_list = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
            "operationAmount": {"amount": 16210.0, "currency": {"name": "Sol", "code": "PEN"}},
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
            "operationAmount": {"amount": 29740.0, "currency": {"name": "Peso", "code": "COP"}},
        },
        {
            "id": 593027.0,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
            "operationAmount": {"amount": 30368.0, "currency": {"name": "Shilling", "code": "TZS"}},
        },
        {
            "id": 366176.0,
            "state": "EXECUTED",
            "date": "2020-08-02T09:35:18",
            "from": "Discover 0325955596714937",
            "to": "Visa 3820488829287420",
            "description": "Перевод с карты на карту",
            "operationAmount": {"amount": 29482.0, "currency": {"name": "Rupiah", "code": "IDR"}},
        },
        {
            "id": 5380041.0,
            "state": "CANCELED",
            "date": "2021-02-01T11:54:58",
            "from": None,
            "to": "Счет 23294994494356835683",
            "description": "Открытие вклада",
            "operationAmount": {"amount": 23789.0, "currency": {"name": "Peso", "code": "UYU"}},
        },
    ]
    return sample_list


def test_transaction_csv(transaction_tests):
    for _ in range(len(transaction_tests)):
        assert universal_opener(FILE_PATH_CSV)[:5] == transaction_tests


def test_transaction_xlsx(transaction_tests):
    for _ in range(len(transaction_tests)):
        assert universal_opener(FILE_PATH_XLSX)[:5] == transaction_tests
