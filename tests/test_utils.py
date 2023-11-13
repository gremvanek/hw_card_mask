import json
import pathlib
import random

file_path = pathlib.Path('data', 'operations.json')


def test_my_function():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            operations = json.load(f)
            operation_dict = random.choice(operations)
            currency_code = operation_dict['operationAmount']['currency']['code']
    except ValueError as e:
        if currency_code != 'RUB':
            assert True, e
            'Транзация выполнена не в рублях. Укажите транзакцию в рублях'
        return True
    except Exception as e:
        if e == float:
            assert True, e
