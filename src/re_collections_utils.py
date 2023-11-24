import pathlib
import re

from typing import Generator, Any
from collections import Counter
from src.panda import universal_opener

ROOT_PATH = pathlib.Path(__file__).parent.parent
FILE_PATH_CSV = ROOT_PATH.joinpath('data_files', 'transactions_2.csv')
FILE_PATH_XLSX = ROOT_PATH.joinpath('data_files', 'transactions_excel.xlsx')
FILE_PATH_JSON = ROOT_PATH.joinpath('data_files', 'operations.json')
dict_list = universal_opener(FILE_PATH_CSV)
description_dict = {'Перевод организации': 0, 'Перевод с карты на карту': 0, 'Открытие вклада': 0,
                    'Перевод со счета на счет': 0}


def function_for_search(dict_list: list[dict], search_string: Any = None) -> Generator:
    """
    Функция для поиска операций.
    :return: list[dict]
    """
    for dicts in dict_list:
        for key, value in dicts.items():
            pattern = re.compile(search_string).search(str(value) or str(key))
            if pattern:
                search_string_dict = {'id': dicts['id'],
                                      'date': dicts['date'], 'operationAmount': dicts['operationAmount'],
                                      'state': dicts['state'], 'from': dicts['from'], 'to': dicts['to'],
                                      'description': dicts['description']}
                yield search_string_dict
            else:
                pass


def function_for_count(dict_list: list[dict], description_dict: Any = None) -> Any:
    """
    Функция для поиска операций.
    :return: list[dict]
    """
    descriptions = [x["description"] for x in dict_list if x["description"] in description_dict.keys()]
    counter = Counter(descriptions)
    return counter
