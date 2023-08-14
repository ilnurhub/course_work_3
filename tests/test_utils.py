from course_work_3.utils.utils import json_file_manager, load_json, sort_list_of_dicts, title_and_account, hide_account, \
    split_four_card_number, find_transfer_date, create_output, create_several_executed_outputs


def test_json_file_manager():
    assert json_file_manager(r'tests\test_json.json') == [{"id": 441945886, "state": "EXECUTED"},
                                                          {"id": 41428829, "state": "EXECUTED"}]


def test_load_json():
    assert load_json('test_json.json', directory='tests') == [{"id": 441945886, "state": "EXECUTED"},
                                                              {"id": 41428829, "state": "EXECUTED"}]


def test_sort_list_of_dicts():
    assert sort_list_of_dicts([{'id': 1, 'date': '2009-12-08'}, {'id': 2, 'date': '2023-06-15'}], 'date') == \
           [{'id': 2, 'date': '2023-06-15'}, {'id': 1, 'date': '2009-12-08'}]


def test_title_and_account():
    assert title_and_account('Visa Classic 6831982476737658') == ('Visa Classic', '6831982476737658')


def test_hide_account():
    assert hide_account('6831982476737658') == '683198******7658'
    assert hide_account('48894435694657014368') == '**4368'


def test_split_four_card_number():
    assert split_four_card_number('6831982476737658') == '6831 9824 7673 7658'


def test_find_transfer_date():
    assert find_transfer_date('2019-08-26T10:50:58.294041') == '26.08.2019'


def test_create_output():
    assert create_output({'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
                          'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
                          'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}) == """08.12.2019 Открытие вклада
  -> Счет **5907
41096.24 USD"""
    assert create_output({"id": 518707726, "state": "EXECUTED", "date": "2018-11-29T07:18:23.941293",
                          "operationAmount": {"amount": "3348.98", "currency": {"name": "USD", "code": "USD"}},
                          "description": "Перевод с карты на карту", "from": "MasterCard 3152479541115065",
                          "to": "Visa Gold 9447344650495960"}) == """29.11.2018 Перевод с карты на карту
MasterCard 3152 47** **** 5065 -> Visa Gold 9447 34** **** 5960
3348.98 USD"""


def test_create_several_outputs():
    assert create_several_executed_outputs([{"id": 518707726, "state": "EXECUTED", "date": "2018-11-29T07:18:23.941293",
                                             "operationAmount": {"amount": "3348.98",
                                                                 "currency": {"name": "USD", "code": "USD"}},
                                             "description": "Перевод с карты на карту",
                                             "from": "MasterCard 3152479541115065",
                                             "to": "Visa Gold 9447344650495960"}], output_counts=1) is None
