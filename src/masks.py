def mask_card(card_mask: str, card_name: str, card_names: list) -> str:
    """Возвращаем результат в необходимом виде - Название карты и
    замаскированный номер
    XXXX XX** **** XXXX
    :param card_mask
    : Номер для маскирования
    :return: Маскированный по правилу номер
    """
    for _ in card_names:
        if card_name not in card_names:
            print("Тип карты неизвестен")
            quit()
        else:
            if len(card_mask.replace(" ", "")) != 16:
                print("Введенные данные неверные")
            else:
                pass

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
        return "**" + check_mask[-4:]
