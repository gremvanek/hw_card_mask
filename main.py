from src.widget import date_optimizer, card_full_printer

card_mask = "Visa Platinum 7000792289606361"
check_mask = "Счет 73654108430135874305"
date = "2018-07-11T02:26:18.671407"

if __name__ == "__main__":
    print(date_optimizer(date))
    print("")
    print(card_full_printer(check_mask))
    print("")
