import logging
import pathlib

masks_log_file = pathlib.Path.cwd() / 'masks.log'
logger = logging.getLogger(__name__)
if masks_log_file.is_file():
    masks_log_file.unlink()
file_handler = logging.FileHandler('masks.log')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(funcName)s %(process)d %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

logger.debug('Run masks.py functions')


def mask_card(card_mask: str) -> str:
    """Возвращаем результат в необходимом виде XXXX XX** **** XXXX
    :param card_mask
    : Номер для маскирования
    :return: Маскированный по правилу номер
    """
    if len(card_mask.replace(" ", "")) != 16:
        return "Введенные данные неверные"
    else:
        return card_mask[0:4] + " " + card_mask[4:6] + "** **** " + card_mask[-4:]


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
