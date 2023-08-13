from utils.utils import load_json


def test_load_json():
    assert load_json('data/test_json.json') == [{"id": 441945886, "state": "EXECUTED"},
                                                {"id": 41428829, "state": "EXECUTED"}]
