import pathlib


from src.panda import universal_opener
from src.re_collections_utils import function_for_count, function_for_search


file_path = pathlib.Path('data_files', 'operations.json')
card_mask = "Visa Platinum 7000792289606361"
check_mask = "Счет 35383033474447895560"
date_for_func = "2018-07-11T02:26:18.671407"
state_list_dict = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]
transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)
ROOT_PATH = pathlib.Path(__file__).parent
FILE_PATH_CSV = ROOT_PATH.joinpath('data_files', 'transactions_2.csv')
FILE_PATH_XLSX = ROOT_PATH.joinpath('data_files', 'transactions_excel.xlsx')
FILE_PATH_JSON = ROOT_PATH.joinpath('data_files', 'operations.json')
dict_list = universal_opener(FILE_PATH_CSV)
description_dict = {'Перевод организации': 0, 'Перевод с карты на карту': 0, 'Открытие вклада': 0,
                    'Перевод со счета на счет': 0}
search_string = "Перевод организации"
if __name__ == "__main__":
    # print(date_optimizer(date_for_func))
    # print("")
    # print(card_full_printer(card_mask))
    # print("")
    # print(list_dict_sort(state_list_dict, 'CANCELED'))
    # print("")
    # print(list_date_sort(state_list_dict, False))
    # print("")
    # usd_transactions = filter_by_currency(transactions, "RUB")
    # descriptions = transaction_descriptions(transactions)
    #
    # for _ in range(2):
    #     print(next(usd_transactions)["id"])
    # print("")
    # for _ in range(5):
    #     print(next(descriptions))
    # print("")
    # for card_number in card_number_generator(1234432112344321, 1234432112344329):
    #     print(card_number)
    # transaction = random.choice(json_file_read(file_path))
    # print(my_transaction_func(transaction))
    print(function_for_count(dict_list, description_dict))
    print(list(function_for_search(dict_list, search_string)))
