import requests


response = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
data = response.json()

for dict in data:
    if dict['txt'] == "Долар США":
        USD = dict['rate']