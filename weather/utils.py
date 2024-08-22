import requests

def fetch_weather_data(city):
    api_key = 'f7ac9050dcb74700ac890627242108'
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()

    return {
        'city': city,
        'temperature': data['current']['temp_c'],
        'humidity': data['current']['humidity'],
        'description': data['current']['condition']['text'],
        'timestamp': data['current']['last_updated']
    }