import requests

url = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "API_KEY"


def get_weather(city: str, api_key: str) -> None:

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ru'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        return {
            "temperature": data['main']['temp'],
            "description": data['weather'][0]['description'],
            "feels_like": data['main']['feels_like'],
            "humidity": data['main']['humidity']
        }
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            raise Exception(f"Ошибка: Город '{city}' не найден.")
        elif response.status_code == 401:
            raise Exception("Ошибка: Неверный API ключ.")
        else:
            raise Exception(f"HTTP ошибка: {http_err}")


def print_weather(city: str, weather):
    print(f"Погода в городе: {city}")
    print(f"Температура: {weather["temperature"]}°C")
    print(f"Ощущается как: {weather["feels_like"]}°C")
    print(f"Описание: {weather["description"]}")
    print(f"Влажность: {weather["humidity"]}%")


if __name__ == "__main__":
    city = input("Введите название города: ").strip()

    try:
        weather = get_weather(city, API_KEY)
        print_weather(city, weather)
    except Exception as err:
        print(err)
