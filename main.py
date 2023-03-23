import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

APP_ID = "c775bd28"
API_KEY = "fd14d8708a1ece7cc52a60ed5de00def"
Authorization_Header = "Basic bWFoZXNoOm1haGVzaEA3Nzc="  # for sheety
Username = "mahesh"  # sheety username
Password = "mahesh@222"  # sheety password

exercise_end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"  # nutrinox nlp endpoint

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
user_params = {
    'query': input("Tell me which exercises you did: "),
    'gender': 'male',
    'age': 18,
}


response = requests.post(url=exercise_end_point, json=user_params, headers=headers)
exercises_json = response.json()
# print(response.json())

today = datetime.now()

sheety_end_point = "https://api.sheety.co/975d35589e9daadb583eefe5f77bba73/workoutTracking/workouts"

sheety_headers = {
    "Authorization": Authorization_Header
}

for exercise in exercises_json['exercises']:
    workout_params = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    sheet_response = requests.post(url=sheety_end_point, json=workout_params, headers=sheety_headers, auth=HTTPBasicAuth(Username, Password))
    print(sheet_response.text)
