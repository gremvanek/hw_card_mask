from src.processing import list_dict_sort, list_date_sort, sum_divisible_by_3_or_5, check_email
from src.widget import date_optimizer, card_full_printer

card_mask = "Visa Platinum 7000792289606361"
check_mask = "Счет 35383033474447895560"
date = "2018-07-11T02:26:18.671407"
state_list_dict = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]
lst = [1, 2, 3, 4, 5]
email = 'choobaiz@sveta.net'

if __name__ == "__main__":
    print(date_optimizer(date))
    print("")
    print(card_full_printer(check_mask))
    print("")
    print(list_dict_sort(state_list_dict, 'CANCELED'))
    print("")
    print(list_date_sort(state_list_dict, False))
    print("")
    print(sum_divisible_by_3_or_5(lst))
    print("")
    print(check_email(email))
