from course_work_3.utils.utils import load_json, sort_list_of_dicts, title_and_account


def test_load_json():
    assert load_json('course_work_3/data/test_json.json') == [{"id": 441945886, "state": "EXECUTED"},
                                                              {"id": 41428829, "state": "EXECUTED"}]


def test_sort_list_of_dicts():
    assert sort_list_of_dicts([{'id': 1, 'date': '2009-12-08'}, {'id': 2, 'date': '2023-06-15'}], 'date') == \
           [{'id': 2, 'date': '2023-06-15'}, {'id': 1, 'date': '2009-12-08'}]


def test_title_and_account():
    assert title_and_account('Visa Classic 6831982476737658') == ('Visa Classic', '6831982476737658')
