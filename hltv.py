import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.hltv.org/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    newshltv = soup.find_all("div", {"class": "standard-box standard-list"})
    if newshltv:
        newsline = newshltv[0].find("div", {"class": "newsline article"})
        newstext = newshltv[0].find("div", {"class": "newstext"})
        if newstext:
            print(newstext.text)
        else:
            print('-')
    else:
        print('-')
else:
    print('Ошибка при получении страницы')