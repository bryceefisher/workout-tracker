from datetime import datetime
import requests

# Constants

CURRENT_DATE = datetime.now().strftime("%m%d%Y")
CURRENT_TIME = datetime.now().strftime("%H:%M")
API_ID = "Nutritionix API ID"
API_KEY = "Nutritionix API Key"
GENDER = "Your Gender"
AGE = Your Age (int)
WEIGHT = Your Weight in Kg (int)
HEIGHT = Your Height in cm (int)

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "hYour Sheety endpint"

nutritionix_headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

nutritionix_config = {
    "query": input("What workouts would you like to track? "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

nutritionix_response = requests.post(nutritionix_endpoint, json=nutritionix_config, headers=nutritionix_headers)
nut_list = nutritionix_response.json()

for user_workouts in nut_list["exercises"][:]:
    user_workout = {
        "date": CURRENT_DATE,
        "time": CURRENT_TIME,
        "exercise": user_workouts['user_input'].title(),
        "duration": user_workouts["duration_min"],
        "calories": user_workouts["nf_calories"]
    }
    workout = {
        "workout": user_workout

    }
    sheety_response = requests.post(sheety_endpoint, json=workout)
    print(sheety_response.text)
