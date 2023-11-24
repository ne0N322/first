import requests
from bs4 import BeautifulSoup
import sqlite3


connection = sqlite3.connect("weather.db", 5)
cur = connection.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS weather_dz (weath TEXT);")
connection.commit()


response = requests.get("https://weather.com/uk-UA/weather/today/l/00943a753bfc75f7ba41ac766b15583ee29dfd707f24e8699ef7c324bf3e68da")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list_timestamp = soup.find_all("div", {"class": "CurrentConditions--header--kbXKR"})
    if soup_list_timestamp:
        res_timestamp = soup_list_timestamp[0].find("span")
    else:
        res_timestamp = "weath"

    print(res_timestamp.text)

    soup_list = soup.find_all("div", {"class": "CurrentConditions--primary--2DOqs"})
    res = soup_list[0].find("span")
    print("Температура - " + res.text)

    cur.execute("INSERT INTO weather_dz (weath) VALUES (?);", (res_timestamp.text + " " + res.text,))

cur.execute("SELECT weath FROM weather_dz;")
res = cur.fetchall()
print(res)

connection.close()
