from src.masks import mask_card, mask_check
from src.widget import date_optimizer, card_full_printer

card = "Visa Platinum 7000792289606361"
check_mask = "Счет 73654108430135874305"
date = "2018-07-11T02:26:18.671407"
new_date = ""
card_list = card.split(' ')
check_mask_list = check_mask.split(' ')

print(date_optimizer(date))
print('')
print(card_full_printer(card_list))
print(f"{check_mask_list[0]} {mask_check(check_mask_list)}")
