import requests

api_key = "4f23f5a59d41d2e69452a7031b48dc89"


def get_data(place, forecastdays):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    content = response.json()

    nr_value = 8 * forecastdays
    filtered_data = content['list'][:nr_value]

    return filtered_data
