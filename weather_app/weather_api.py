import requests
import json
from classes import Weather, datetime
from dotenv import load_dotenv
import os

load_dotenv()

def get_weather(city_name: str, mock: bool = True) -> dict:
    if mock:
        with open("dummy_data.json") as file:
            return json.load(file)
    
    params: dict = {"q": city_name, "appid": os.getenv("API_KEY"), "units": "metric"}
    request = requests.get(url=os.getenv("BASE_URL"), params=params)
    data: dict = request.json()
    
    return data

def get_weather_details(weather: dict) -> [Weather]:
    days: list[dict] = weather.get("list")
    
    if not days:
        raise Exception(f"Problem with json: {weather}")
    
    list_of_weather: list[Weather] = []
    
    for day in days:
        w: Weather = Weather(date=datetime.fromtimestamp(day.get("dt")),
                             details=(details:=day.get("main")),
                             temp=details.get("temp"),
                             weather=(weather:=day.get("weather")),
                             description=weather[0].get("description"))
        list_of_weather.append(w)
    
    return list_of_weather