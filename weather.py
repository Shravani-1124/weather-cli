import requests
import requests
import os
from dotenv import load_dotenv

load_dotenv()
city = input("Enter your city here:")

api_key= os.getenv("WEATHER_API_KEY")
print(f"You enetered: {city}")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {description}")


except requests.HTTPError:
    print("City not found or API request was unsuccessful.")

except requests.RequestException:
    print("Could not connect to the weather service.")



