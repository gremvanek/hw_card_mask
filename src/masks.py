def mask_card(card_mask: str, card_name: str) -> str:
    """Возвращаем результат в необходимом виде XXXX XX** **** XXXX
    :param card_name: in main.py
    :param card_mask
    : Номер для маскирования
    :return: Маскированный по правилу номер
    """
    if len(card_mask.replace(" ", "")) != 16:
        return "Введенные данные неверные"
    else:
        return card_name + " " + card_mask[0:4] + " " + card_mask[4:6] + "** **** " + card_mask[-4:]


def mask_check(check_mask: str) -> str:
    """Возвращаем результат в необходимом виде **XXXX
    :param check_mask
    : Номер для маскирования
    :return: Маскированный по правилу номер
    """
    if len(check_mask.replace(" ", "")) != 20:
        return "Введенные данные неверные"
    else:
        return "Счет **" + check_mask[-4:]
