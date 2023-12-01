import requests
from bs4 import BeautifulSoup
# import sqlite3

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get("https://www.hltv.org/", headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    newshltv = soup.find_all("div", {"class": "standard-box standard-list"})
    if newshltv:
        newsline = soup.find_all("div", {"class": "newsline article"})
        newstext = soup.find_all("div", {"class": "newstext"})
        if newstext:
            for news in newstext:
                news_text = news.get_text(strip=True)
                print(news_text)
        else:
            print('-')
    else:
        print('-')
else:
    print('Ошибка при получении страницы')