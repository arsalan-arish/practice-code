import requests
import json
import os

APP_KEY = os.getenv()

params = {
    "app_key": APP_KEY
}

# ! 1st experiment
# url = "https://api.tfl.gov.uk/Line/Mode/tube"


# ans1 = requests.get(url, params=params)

# print(ans1.status_code)

# with open("response1.json", "w") as f1:
#     f1.write(json.dumps(ans1.json(), indent=4))


# ! 2nd experiment
# stop_id = "490008660N"
# url = f"https://api.tfl.gov.uk/StopPoint/{stop_id}/Arrivals"

# ans2 = requests.get(url, params=params)

# print(ans2.status_code)

# with open("response2.json", "w") as f2:
#     f2.write(json.dumps(ans2.json(),indent=4))


# ! 3rd experiment
