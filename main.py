from src.masks import mask_card, mask_check
from src.widget import date_optimizer, card_full_printer

card = "Visa Platinum 7000792289606361"
check_mask = "Счет 73654108430135874305"
date = "2018-07-11T02:26:18.671407"
new_date = ""
new_card_mask = mask_card(card)
new_mask_check = mask_check(check_mask)

print(date_optimizer(date))
print('')
card_full_printer(card, check_mask)
