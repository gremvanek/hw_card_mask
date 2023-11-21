import logging
import pathlib

masks_log_file = pathlib.Path.cwd() / 'masks.log'
logger = logging.getLogger(__name__)
if masks_log_file.is_file():
    masks_log_file.unlink()
file_handler = logging.FileHandler('masks.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

logger.info('Run masks.py functions')


def mask_card(card_mask: str) -> str:
    """Возвращаем результат в необходимом виде XXXX XX** **** XXXX
    :param card_mask
    : Номер для маскирования
    :return: Маскированный по правилу номер
    """
    logger_mask_card = logging.getLogger(__name__)
    logger_mask_card.info('Запуск функции для маскирования карты.')
    if len(card_mask.replace(" ", "")) != 16:
        logger_mask_card.error('ValueError: Номер карты неверный')
        return "Введенные данные неверные"
    else:
        logger_mask_card.info(f"Номер карты: {card_mask[0:4] + ' ' + card_mask[4:6] + '** **** ' + card_mask[-4:]}")
        return card_mask[0:4] + ' ' + card_mask[4:6] + '** **** ' + card_mask[-4:]


def mask_check(check_mask: str) -> str:
    """Возвращаем результат в необходимом виде **XXXX
    :param check_mask
    : Номер для маскирования
    :return: Маскированный по правилу номер
    """
    logger_mask_check = logging.getLogger(__name__)
    logger_mask_check.info('Запуск функции для маскирования счёта.')
    if len(check_mask.replace(" ", "")) != 20:
        logger_mask_check.error('ValueError: Номер счёта неверный')
        return 'Введенные данные неверные'
    else:
        logger_mask_check.info(f"Номер счёта: {'**' + check_mask[-4:]}")
        return '**' + check_mask[-4:]
