import requests
import datetime
from aiogram import executor, Dispatcher, types, Bot
from aiogram.utils.markdown import hbold
from datetime import datetime
telegram_token_api = '5396208640:AAHL0tEkZNVblhyMCYqCSF0pUd9EPRhJ4hE'
open_weather_token = '7c571b5581ec40b345fb3864683ba49e'

bot = Bot(token=telegram_token_api)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await message.reply(f"Добрий день {message.from_user.full_name}. Оберіть функціонал бота:\n"
                        f"/weather -  Погода в будь якому місті планети\n"
                        f"/currency - Курс до Доллара/Євро\n")


@dp.message_handler(commands='currency')
async def currency(message: types.Message):
    response = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
    data = response.json()
    for dict in data:
        if dict['txt'] == "Долар США":
            USD = dict['rate']
            await message.reply(f'Курс долара до гривні: 1$ : {USD} грн\n')
        elif dict['txt'] == "Євро":
            EUR = dict['rate']
            await message.reply(f'Курс євро до гривні: 1€ : {EUR} грн\n')


@dp.message_handler(commands='weather')
async def weather(message: types.Message):
    await message.reply('Введіть місто, в якому ви хочете дізнатися погоду')


@dp.message_handler()
async def get_message(message: types.Message):
        try:
            response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric')
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

            await message.reply(f"***{hbold(datetime.now().strftime('%Y-%m-%d %H:%M'))}***\n"
                  f"Погода у місті: {requested_city}({country})\nТемпература: {current_temperature}C° {weather_description}, Відчувається як: {current_temperature_feels_like} C° \n"
                  f"Вологість: {humidity}%\nТиск: {pressure} мм.рт.ст\nВітер: {current_weather_wind} м/с\n"
                  f"Схід сонця: {iso_sunrise_time}\nЗахід солнца: {iso_sunset_time}\nПродовжуваність доби: {length_of_the_day}\n"
                  f"Гарного дня!😎"
                  )
        except:
            await message.reply('Перевірте правильність написаної назви міста')

if __name__ == '__main__':
    executor.start_polling(dp)
