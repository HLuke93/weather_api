import requests
from datetime import datetime

api_key = "0a83a5d02d85430986aa98fc001d9504"
location = input("Please enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key

api_link = requests.get(complete_api_link)
api_data = api_link.json()

print(api_data)
