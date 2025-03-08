import json
import requests
from datetime import datetime


class SomeResourseClient:
    def __init__(self, url):
        self.url = url

    def __user_get_status(self, user_hash):
        resp = requests.get(f"{self.url}/web/2/user/get-status/{user_hash}")
        json_data = json.loads(resp.text)
        return json_data

    def get_user_last_action_time(self, user_hash):
        json_data = self.__user_get_status(user_hash)
        last_action_time = json_data["lastActionTime"]
        time_diff = json_data["timeDiff"]
        return datetime.fromtimestamp(last_action_time - time_diff)


if __name__ == "__main__":
    some_resourse_client = SomeResourseClient("https://www.avito.ru/")
    print(some_resourse_client.get_user_last_action_time("5d4c951270e4c82d078efcd7d5f911e6"))
    c = 1
