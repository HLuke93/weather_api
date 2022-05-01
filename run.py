import requests
from datetime import datetime

api_key = "0a83a5d02d85430986aa98fc001d9504"
location = input("Please enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key

api_link = requests.get(complete_api_link)
api_data = api_link.json()


# EXTRACT JSON DATA and Create Variables to store and display data

if api_data["cod"] == "404":
    print("Invalid city, please check city name")
else:

    temp_city = ((api_data["main"]["temp"]) - 273.15)
    weather_description = api_data["weather"][0]["description"]
    humidity = api_data["main"]["humidity"]
    wind_speed = api_data["wind"]["speed"]
    date_time = datetime.now().strftime("%d %b %Y | %I %M %S %p")

    print("_________________________________________")
    print("Weather stats for - {} ||  {}".format(location.upper(), date_time))
    print("_________________________________________")

    print("Current temperature is {:.2f} deg C".format(temp_city))
    print("Current weather desc  :",weather_description)
    print("Current humidity  :",humidity, "%")
    print("Current wind speed  :",wind_speed, "kmph")


