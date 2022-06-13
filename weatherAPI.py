import requests
import json
API_KEY = "ff8365564e454a3bb1b93907223005"
BASE_URL = "https://api.weatherapi.com/v1"
LOCATION = "Bern"
PARAMETER = "?key="+API_KEY+"&q="+LOCATION


def get_weather(path):
    response = requests.get(BASE_URL + path + PARAMETER)
    return json.loads(response.content)
