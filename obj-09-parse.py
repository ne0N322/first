import requests
from bs4 import BeautifulSoup

print()
# response = requests.get("https://coinmarketcap.com/")
# print(response.status_code)
# print(response.content)
# print(f"Datatype – {type(response.text)}")

"""
str_parse = response.text.split('<a href="/currencies/bitcoin/#markets" class="cmc-link">')
for elem_1 in str_parse:

    if elem_1.startswith("<span>"):
        for elem_2 in elem_1.split("</span>"):
            if elem_2.startswith("$") and elem_2[2].isdigit():
                print("Temp", elem_2)

    print(elem_1)
"""

response = requests.get("https://weather.com/uk-UA/weather/today/l/00943a753bfc75f7ba41ac766b15583ee29dfd707f24e8699ef7c324bf3e68da")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("div", {"class": "CurrentConditions--primary--2DOqs"})
    res = soup_list[0]  .find("span")
    print(soup_list)


"""
response = requests.get("https://coinmarketcap.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    # <a href="/currencies/bitcoin/#markets" class="cmc-link"><span>$36,535.39</span></a>
    soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/#markets"})
    res = soup_list[0].find("span")
    print("Bitcoin =", res.text)
"""


