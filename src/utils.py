import json
import pathlib
from typing import Any
import logging

file_path = pathlib.Path('data', 'operations.json')
utils_log_file = pathlib.Path.cwd() / 'utils.log'
logger = logging.getLogger(__name__)
if utils_log_file.is_file():
    utils_log_file.unlink()
file_handler = logging.FileHandler('utils.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

logger.info('Run utils.py functions')


def json_file_read(file_name: Any) -> Any:
    """
    Функция для чтения файла json.
    :return: dict
    """
    file_name = file_path
    logger_json = logging.getLogger(__name__)
    logger_json.info('Открытие файла json.')
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            logger_json.info("json_file_read successful with result: operations.json.")
            operations = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError) as e_1:
        if FileNotFoundError == e_1:
            logger_json.error("FileNotFoundError result: []")
        else:
            logger_json.error("json.decoder.JSONDecodeError result: []")
        operations = []
    return operations


def my_transaction_func(transaction: dict) -> float | str:
    """
    Функция выполняет транзакцию в рублях.
    :rtype: Any
    """
    logger_transaction = logging.getLogger(__name__)
    logger_transaction.info('Запуск функции для вывода транзакции в рублях.')
    currency_code = transaction['operationAmount']['currency']['code']
    amount_transaction = transaction['operationAmount']['amount']
    if currency_code != 'RUB':
        logger_transaction.error('ValueError: Транзакция выполнена не в рублях. Укажите транзакцию в рублях')
        raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
    else:
        logger_transaction.info(f"Транзакция выполнена в рублях. result: {amount_transaction}")
        return float(amount_transaction)
