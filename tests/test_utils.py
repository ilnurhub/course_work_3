from course_work_3.utils.utils import load_json


def test_load_json():
    assert load_json('course_work_3/data/test_json.json') == [{"id": 441945886, "state": "EXECUTED"},
                                                {"id": 41428829, "state": "EXECUTED"}]
