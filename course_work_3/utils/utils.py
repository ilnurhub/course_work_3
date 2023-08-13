import json


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
