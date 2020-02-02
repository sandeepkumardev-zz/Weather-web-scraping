import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get('https://weather.com/en-IN/weather/tenday/l/4c2a12bd2ab64116b9017d2f55d601f8662c908d78f9fc03d1c301f3f752644d')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find_all(class_="clickable closed")

day_name = [item.find(class_="date-time").get_text() for item in week]
day_date = [item.find(class_="day-detail clearfix").get_text() for item in week]
day_desc = [item.find(class_="description").get_text() for item in week]
temp_high = [item.find(class_="temp").get_text()[:-2] for item in week]
temp_low = [item.find(class_="temp").get_text()[3:] for item in week]
day_rain = [item.find(class_="precip").get_text() for item in week]
day_wind = [item.find(class_="wind").get_text() for item in week]
day_nami = [item.find(class_="humidity").get_text() for item in week]

weather_stuff = pd.DataFrame(
    {
        "Day  " : day_name,
        "Date " : day_date,
        "Decription" : day_desc,
        "High" : temp_high,
        "Low" : temp_low,
        " Rain" : day_rain,
        "Wind     " : day_wind,
        " HUMIDITY": day_nami
    }
)

print(weather_stuff)

