import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather_and_predict_diseases(lat, lon):
    """
    Fetch weather data from OpenWeatherMap API for the given latitude and longitude,
    and predict potential fruit diseases based on weather conditions.
    
    Args:
        lat (float): Latitude coordinate.
        lon (float): Longitude coordinate.
        api_key (str): API key for OpenWeatherMap.

    Returns:
        dict: Weather details and predicted diseases.
    """
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error fetching weather data:", response.json())
        return None
    
    weather_data = response.json()
    forecast = weather_data['list'][:5]  # Next 5 periods (each 3 hours)
    
    temps = [period['main']['temp'] for period in forecast]
    avg_temp = sum(temps) / len(temps)
    humidities = [period['main']['humidity'] for period in forecast]
    avg_humidity = sum(humidities) / len(humidities)
    precipitations = [period.get('rain', {}).get('3h', 0) for period in forecast]
    total_precip = sum(precipitations)
    
    diseases = []
    if 10 <= avg_temp <= 20 and total_precip > 10:
        diseases.append("Apple Scab")
    if avg_humidity > 70 and avg_temp > 20:
        diseases.append("Fire Blight")
    if total_precip < 5 and 15 <= avg_temp <= 25:
        diseases.append("Powdery Mildew")
    
    return avg_temp, avg_humidity, total_precip, diseases
