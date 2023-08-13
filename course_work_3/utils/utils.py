import json


def load_json(file):
    """
    Читает данные из файла в формате JSON и возвращает список
    """
    with open(file, 'r', encoding='utf-8') as f:
        lst = json.load(f)
    return lst
