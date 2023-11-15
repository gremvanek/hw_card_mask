import json
import pathlib
from typing import Any
import logging

file_path = pathlib.Path('data', 'operations.json')
utils_log_file = pathlib.Path.cwd() / 'utils.log'
logger = logging.getLogger(__name__)
if utils_log_file.is_file():
    utils_log_file.unlink()
file_handler = logging.FileHandler('utils.log')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(funcName)s %(process)d %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

logger.debug('Run utils.py functions')


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
