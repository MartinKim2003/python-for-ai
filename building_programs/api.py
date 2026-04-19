import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

data

# The API sends back data in JSON format (like a Python dictionary):
 
{
    'latitude': 48.84,
    'longitude': 2.36,
    'timezone': 'GMT',
    'elevation': 46.0,
    'current_units': {
        'temperature_2m': '°C'
    },
    'current': {
        'time': '2025-08-01T08:30',
        'temperature_2m': 20.0
    }
}

# The temperature is nested in current, so to get it: 
temperature = data['current']['temperature_2m']
print(f"Temperature in Paris: {temperature}°C")
# Output: Temperature in Paris: 20.0°C