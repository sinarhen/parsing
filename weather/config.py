import requests
from datetime import datetime

open_weather_token = '7c571b5581ec40b345fb3864683ba49e'


def get_weather(city, token):

    try:
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric')
        data = response.json()

        """
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"""""
        requested_city = data['name']
        country = data['sys']['country']
        current_temperature = data['main']['temp']
        current_temperature_feels_like = data['main']['feels_like']
        current_weather_wind = data['wind']['speed']
        iso_sunrise_time = datetime.fromtimestamp(data['sys']['sunrise'])
        iso_sunset_time = datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = iso_sunset_time - iso_sunrise_time
        weather_description = data["weather"][0]["main"]
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']

        print(f"***{datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода у місті: {requested_city}({country})\nТемпература: {current_temperature}C° {weather_description}, Відчувається як:{current_temperature_feels_like} \n"
              f"Вологість: {humidity}%\nТиск: {pressure} мм.рт.ст\nВітер: {current_weather_wind} м/с\n"
              f"Схід сонця: {iso_sunrise_time}\nЗахід солнца: {iso_sunset_time}\nПродовжуваність доби: {length_of_the_day}\n"
              f"Гарного дня!"
              )

    except Exception as ex:
        print("Проверьте название города")


def main():
    city = input('Город')
    print(get_weather(city, token=open_weather_token))


if __name__ == '__main__':
    main()
