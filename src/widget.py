from src.masks import mask_card, mask_check


def date_optimizer(date: str) -> str:
    """
    Для выборки нужных символов из строки с датой
    :param date: str :return: str
    """
    return date[8:10] + "." + date[5:7] + "." + date[0:4]


def card_full_printer(arg: str) -> str:
    arg_new = arg.split()
    if "Счет" in arg_new:
        elon_mask = mask_check(arg_new[-1])
        return arg_new[0] + " " + elon_mask
    else:
        elon_card = mask_card(arg_new[-1])
        new_card_name = " ".join(arg_new[:-1])
        return new_card_name + " " + elon_card
