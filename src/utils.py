import json
import pathlib
from typing import Any

file_path = pathlib.Path('data_files', 'operations.json')


def json_file_read(file_name: Any) -> Any:
    """
    Функция для чтения файла json.
    :return: dict
    """
    file_name = file_path
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            operations = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        operations = []
    return operations


def my_transaction_func(transaction: dict) -> float | str:
    """
    Функция выполняет транзакцию в рублях.
    :rtype: Any
    """
    currency_code = transaction['operationAmount']['currency']['code']
    amount_transaction = transaction['operationAmount']['amount']
    if currency_code != 'RUB':
        raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
    else:
        return float(amount_transaction)
