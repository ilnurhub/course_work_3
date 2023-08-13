import json
from datetime import date


def load_json(file):
    """
    Читает данные из файла в формате JSON и возвращает список
    """
    with open(file, 'r', encoding='utf-8') as f:
        lst = json.load(f)
    return lst


def sort_list_of_dicts(user_list, sort_key, rev=True):
    """
    Сортирует список словарей по заданному ключу
    """
    sorted_user_list = sorted(user_list, key=lambda d: d.get(sort_key, '0'), reverse=rev)
    return sorted_user_list


def title_and_account(title_account):
    """
    Возвращает название счета и номер счета
    """
    *title_parts, account = title_account.split(' ')
    title = ' '.join(title_parts)
    return title, account


def hide_account(account):
    """
    Маскирует номер карты или счета
    """
    if len(account) == 16:
        masked_account = account[0:6] + '*' * (len(account) - 10) + account[-4:]
    else:
        masked_account = '*' * 2 + account[-4:]
    return masked_account


def split_four_card_number(card_number):
    """
    Разбивает номер карты по блокам по 4 цифры
    """
    list_of_blocks = []
    i = 0
    while i < len(card_number):
        list_of_blocks.append(card_number[i:i + 4])
        i += 4
    four_digits_blocks = ' '.join(list_of_blocks)
    return four_digits_blocks


def find_transfer_date(date_time):
    """
    Возвращает дату перевода, представленную в формате ДД.ММ.ГГГГ
    """
    transfer_date = date_time.split('T')[0]
    the_date = date.fromisoformat(transfer_date)
    date_formatted = the_date.strftime("%d.%m.%Y")
    return date_formatted
