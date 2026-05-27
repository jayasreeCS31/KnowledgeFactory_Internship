import requests
from config import WEATHER_API_KEY


def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={WEATHER_API_KEY}"
        f"&units=metric"
    )

    try:

        response = requests.get(url)

        data = response.json()

        if response.status_code != 200:

            return {
                "error":
                data.get(
                    "message",
                    "City not found"
                )
            }

        weather_data = {

            "temperature":
            data["main"]["temp"],

            "condition":
            data["weather"][0]["description"],

            "humidity":
            data["main"]["humidity"]

        }

        return weather_data


    except Exception as e:

        return {
            "error": str(e)
        }