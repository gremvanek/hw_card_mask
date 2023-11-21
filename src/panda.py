import pathlib

import pandas as pd

from typing import Any

ROOT_PATH = pathlib.Path(__file__).parent.parent
FILE_PATH_CSV = ROOT_PATH.joinpath('data_files', 'transactions_2.csv')
FILE_PATH_XLSX = ROOT_PATH.joinpath('data_files', 'transactions_excel.xlsx')
FILE_PATH_JSON = ROOT_PATH.joinpath('data_files', 'operations.json')


def universal_opener(file_name: Any) -> Any:
    """
    Функция для открытия файлов.
    :return: dict
    """
    if '.csv' in str(file_name):
        transactions = pd.read_csv(file_name, sep=';', encoding='utf-8')

    elif '.xlsx' in str(file_name) or '.xls' in str(file_name):
        transactions = pd.read_excel(file_name)
    else:
        raise Exception('Неверный формат файла')

    transaction_dict = transactions.to_dict(orient='records')
    for dicts in transaction_dict:
        for key, value in dicts.items():
            if str(dicts[key]) == 'nan':
                dicts[key] = None
        dicts['operationAmount'] = {'amount': dicts.pop('amount'), 'currency': {'name': dicts.pop('currency_name'),
                                                                                'code': dicts.pop('currency_code')}}
        if dicts['date']:
            dicts['date'] = dicts['date'][:-1]
    return transaction_dict


print(universal_opener(FILE_PATH_CSV))
