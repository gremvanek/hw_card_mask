import re

regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"


def list_dict_sort(state_list_dict: list[dict], key: str) -> list[dict]:
    """
    Функция сортирует значения по ключу, указанному в main.py в аргументе _key_ и возвращает
    последние 2 словаря из списка словарей, в которых находятся необходимые словари
    :param state_list_dict: Список со словарями из дз
    :param key: EXECUTED или CANCELED
    :return: Список со словарями с необходимым параметром state
    """
    sorted_l_d_s = sorted(state_list_dict, key=lambda operator: operator["state"] == key)
    return sorted_l_d_s[-2:]


def list_date_sort(state_list_dict: list[dict], reverse: bool = False) -> list[dict]:
    """
    Функция получает на вход список словарей и сортирует по дате.
    :param state_list_dict: Список со словарями из дз
    :param reverse: По-умолчанию False, но при вызове функции можно менять на True
    :return: Сортированный в зависимости от значения reverse список
    """
    sorted_l_d_s = sorted(state_list_dict, key=lambda operator: operator["date"], reverse=reverse)
    return sorted_l_d_s


def sum_divisible_by_3_or_5(lst: list) -> int:
    """
    Функция принимает на вход список чисел и возвращает сумму всех элементов списка,
    которые делятся на 3 или 5 без остатка.
    """
    result = 0
    for num in lst:
        if num % 3 == 0 or num % 5 == 0:
            result += num
    return result


def check_email(email: str) -> str:
    if re.fullmatch(regex, email):
        return "Верный Email"
    else:
        return "Неверный Email"
