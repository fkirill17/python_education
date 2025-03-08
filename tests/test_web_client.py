from pytest_edu.some_web_client import SomeResourseClient
import responses
from datetime import datetime


@responses.activate
def test_some_web_client():
    valid_json_answer = {
        "lastActionTime": 1741428833,
        "timeDiff": 1000
    }
    responses.add(method=responses.GET, url="https://www.avito.ru/web/2/user/get-status/5d4c951270e4c82d078efcd7d5f911e6",
                  json=valid_json_answer, status=200)
    some_resourse_client = SomeResourseClient("https://www.avito.ru")
    res = some_resourse_client.get_user_last_action_time("5d4c951270e4c82d078efcd7d5f911e6")
    assert res == datetime.fromtimestamp(valid_json_answer["lastActionTime"] - valid_json_answer["timeDiff"])
