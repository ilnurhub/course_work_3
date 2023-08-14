import json
from datetime import date
import os.path


def json_file_manager(file_path):
    """
    Файловый менеджер для чтения json-файла
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        lst = json.load(f)
    return lst


def load_json(file, directory='data'):
    """
    Читает данные из файла в формате JSON и возвращает список
    """
    try:
        file_path = os.path.join('course_work_3', directory, file)
        res = json_file_manager(file_path)
    except FileNotFoundError:
        file_path = os.path.join(directory, file)
        res = json_file_manager(file_path)
    return res


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


def create_output(operation):
    """
    Возвращает вывод для одной операции
    """
    transfer_date = find_transfer_date(operation['date'])
    description = operation['description']
    if 'from' in operation:
        from_title, unmasked_from_account = title_and_account(operation['from'])
        from_account = hide_account(unmasked_from_account)
    else:
        from_title = ''
        from_account = ''
    if len(from_account) == 16:
        from_account = split_four_card_number(from_account)
    to_title, unmasked_to_account = title_and_account(operation['to'])
    to_account = hide_account(unmasked_to_account)
    if len(to_account) == 16:
        to_account = split_four_card_number(to_account)
    operation_amount = f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"
    return f"""{transfer_date} {description}\n{from_title} {from_account} -> {to_title} {to_account}\n{operation_amount}"""


def create_several_executed_outputs(lst, output_counts=5):
    """
    Выводит на экран несколько выполненных операций
    """
    count = 0
    idx = 0
    while count != output_counts:
        if lst[idx]['state'] == 'EXECUTED':
            print(create_output(lst[idx]), end='\n\n')
            count += 1
            idx += 1
        else:
            idx += 1
