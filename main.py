import requests
import os
from datetime import datetime

APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
APP_KEY = os.environ.get("NUTRITIONIX_APP_KEY")

header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "content-type": "application/json"
}

input_data = str(input("Tell me which exercises you did: "))

paramaters = {
    "query": input_data,
}

sheety_endpoint = "https://api.sheety.co/bf38f748919877b14ed25682835c6ea7/myWorkouts/workouts"
sheety_header = {
    "authorization": f"Bearer {os.environ.get('SHEETY_BEARER')}"
}

current = datetime.now()

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=paramaters, headers=header)


workouts = {}
for exercise in response.json()["exercises"]:
    workouts = {
        "workout":{
            "date": current.strftime("%d/%m/%Y"),
            "time": current.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    add_row = requests.post(url=sheety_endpoint, json=workouts, headers=sheety_header)
    print(add_row.status_code)