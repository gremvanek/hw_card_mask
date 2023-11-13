import json
import pathlib
import random

file_path = pathlib.Path('data', 'operations.json')


def json_file_read() -> dict:
    """
    Функция для чтения файла json.
    :return: dict
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            operations = json.load(f)
    except FileExistsError:
        operations = []
    except json.decoder.JSONDecodeError:
        operations = []
    return random.choice(operations)


def my_transaction_func() -> float | str:
    """
    Функция выполняет транзакцию в рублях.
    :rtype: Any
    """
    operation_dict = json_file_read()
    currency_code = operation_dict['operationAmount']['currency']['code']
    amount_transaction = operation_dict['operationAmount']['amount']
    if currency_code != 'RUB':
        message_for_return = "Транзация выполнена не в рублях. Укажите транзакцию в рублях"
        return message_for_return
    else:
        return float(amount_transaction)
