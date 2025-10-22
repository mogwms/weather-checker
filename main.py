import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")
if not api_key:
    raise RuntimeError("API Key Missing")

api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"

city = "New York"

response = requests.get(api_url)
data = response.json()

if "current" in data:
    print(f"Weather in {city}:")
    print(f"{data['current']['temperature']}°C")
else:
    print("Data not Found!")