import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,wind_speed_10m")
    data = response.json()
    return data["current"]["temperature_2m"]

paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

def categoria_temp (temp):
    if temp < 10:
        print(f"Hace frio, lleva abrigo, la temperatura actual es {temp}")
    elif 10 <= temp <= 25:
        print(f"Clima agradable, la temperatura actual es {temp}")
    elif temp > 25:
        print(f"Hace calor, hidratate, la temperatura actual es {temp}")

categoria = categoria_temp(paris_temp)

