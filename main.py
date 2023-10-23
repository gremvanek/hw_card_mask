from src.masks import mask_card, mask_check
from src.widget import date_optimizer, card_full_printer

card_name_list: list[str] = ["Maestro", "MasterCard", "Visa Classic", "Visa Platinum", "Visa Gold"]
card_name = "Visa Platinum"
card_mask = "7000792289606361"
check_mask = "73654108430135874305"
date = "2018-07-11T02:26:18.671407"
new_date = ""
new_card_mask = mask_card(card_mask, card_name)
new_mask_check = mask_check(check_mask)

print(date_optimizer(date))
print('')
print(card_full_printer(card_name_list, card_name, card_mask))
print(mask_check(check_mask))
