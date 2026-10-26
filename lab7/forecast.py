import json
import requests

def weather_in_bergen_next_hour():
    lat = 60.3811725
    lon = 5.3314042
    
    json_weather = requests.get(
            f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}", 
            headers = {
                "User-Agent": "inf100.ii.uib.no nigon5433"
            }
        )

    if json_weather.status_code != requests.codes.ok:
        print(json_weather.text)
        exit(0)

    weather = json.loads(json_weather.text)

    return weather["properties"]["timeseries"][0]["data"]["next_1_hours"]["summary"]["symbol_code"]

print("Været i Bergen neste time:", weather_in_bergen_next_hour())
