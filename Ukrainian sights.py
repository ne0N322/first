import requests
from bs4 import BeautifulSoup
from tkinter import *
import tkinter as tk
from tkinter import messagebox
num_paragraphs = {
    'kiev': [47, 18, 30],
    'kharkiv': [32, 15, 33],
    'lviv': [29, 15, 6],
    'odesa': [50, 14, 15],
    'zaporizhzhia': [40, 12, 24]
}
root = tk.Tk()
root.title('Памятки України')
root.geometry('300x355')

main_frame = tk.Frame(root)
main_frame.pack(pady=10)

class attractions():
    def kievAttractions():
        second_window = tk.Toplevel(root)
        second_frame = tk.Frame(second_window)
        second_frame.pack(pady=10)
        second_window.title("Пам'ятки України")
        try:
            button1 = tk.Button(second_frame, text="Києво-Печерська Лавра")
            button1.pack(side=tk.LEFT, padx=5)
            button1.config(command=info_city.kyiv_kyivopecherskalavra)
        except Exception as exc:
            print(f"Error- {exc}")
        
        try:
            button2 = tk.Button(second_frame, text="Золоті ворота")
            button2.pack(side=tk.LEFT, padx=5)   
            button2.config(command=info_city.kyiv_goldengate)
        except Exception as exc:
            print(f"Error- {exc}")
        try:            
            button3 = tk.Button(second_frame, text="Монумент “Батьківщина-мати”")
            button3.pack(side=tk.LEFT, padx=5) 
            button3.config(command=info_city.kyiv_monumentmotherlandmotherland)
        except Exception as exc:
            print(f"Error- {exc}")        

    def kharkivAttractions():
        second_window = tk.Toplevel(root)
        second_frame = tk.Frame(second_window)
        second_frame.pack(pady=10)
        second_window.title("Пам'ятки України")
        try:
            button1 = tk.Button(second_frame, text="Успенський собор")
            button1.pack(side=tk.LEFT, padx=5)  
            button1.config(command=info_city.kharkiv_assumptioncathedral)
        except Exception as exc:
            print(f"Error- {exc}")        

        try:
            button2 = tk.Button(second_frame, text="Покровський собор")
            button2.pack(side=tk.LEFT, padx=5)   
            button2.config(command=info_city.kharkiv_pokrovskycathedral)
        except Exception as exc:
            print(f"Error- {exc}")  
        
        try:        
            button3 = tk.Button(second_frame, text="Держпром")
            button3.pack(side=tk.LEFT, padx=5) 
            button3.config(command=info_city.kharkiv_derzhprom)
        except Exception as exc:
            print(f"Error- {exc}")         
    
    def lvivAttractions():
        second_window = tk.Toplevel(root)
        second_frame = tk.Frame(second_window)
        second_frame.pack(pady=10)
        second_window.title("Пам'ятки України")
        try:
            button1 = tk.Button(second_frame, text="Львівська ратуша")
            button1.pack(side=tk.LEFT, padx=5)  
            button1.config(command=info_city.lviv_lvivcityhall)
        except Exception as exc:
            print(f"Error- {exc}") 
        
        try:
            button2 = tk.Button(second_frame, text="Архикатедральний Собор Святого Юри")
            button2.pack(side=tk.LEFT, padx=5)   
            button2.config(command=info_city.lviv_archcathedralcathedralofstgeorge)
        except Exception as exc:
            print(f"Error- {exc}") 
        
        try:        
            button3 = tk.Button(second_frame, text="Пам'ятник Степанові Бандері")
            button3.pack(side=tk.LEFT, padx=5) 
            button3.config(command=info_city.lviv_monumenttoastepanbandera)
        except Exception as exc:
            print(f"Error- {exc}") 
    
    def odesaAttractions():
        second_window = tk.Toplevel(root)
        second_frame = tk.Frame(second_window)
        second_frame.pack(pady=10)
        second_window.title("Пам'ятки України")
        try: 
            button1 = tk.Button(second_frame, text="Музей західного і східного мистецтва")
            button1.pack(side=tk.LEFT, padx=5) 
            button1.config(command=info_city.odesa_MuseumofWesternandEasternArt) 
        except Exception as exc:
            print(f"Error- {exc}") 

        try:  
            button2 = tk.Button(second_frame, text="Художній музей")
            button2.pack(side=tk.LEFT, padx=5)   
            button2.config(command=info_city.odesa_ArtMuseum) 
        except Exception as exc:
            print(f"Error- {exc}") 
        
        try:        
            button3 = tk.Button(second_frame, text="Музей сучасного мистецтва")
            button3.pack(side=tk.LEFT, padx=5) 
            button3.config(command=info_city.odesa_MuseumofModernArt) 
        except Exception as exc:
            print(f"Error- {exc}") 
    
    def zaporizhzhiaAttractions():
        second_window = tk.Toplevel(root)
        second_frame = tk.Frame(second_window)
        second_frame.pack(pady=10)
        second_window.title("Пам'ятки України")
        try:
            button1 = tk.Button(second_frame, text="Дніпровська ГЕС")
            button1.pack(side=tk.LEFT, padx=5)  
            button1.config(command=info_city.zaporizhzhia_DniprovskaHPP) 
        except Exception as exc:
            print(f"Error- {exc}") 

        try:
            button2 = tk.Button(second_frame, text="Національний заповідник «Хортиця»")
            button2.pack(side=tk.LEFT, padx=5)   
            button2.config(command=info_city.zaporizhzhia_KhortytsiaNationalReserve) 
        except Exception as exc:
            print(f"Error- {exc}") 
        try:        
            button3 = tk.Button(second_frame, text="Музей історії запорізького козацтва")
            button3.pack(side=tk.LEFT, padx=5)
            button3.config(command=info_city.zaporizhzhia_MuseumoftheHistoryofZaporizhzhyaCossacks)  
        except Exception as exc:
            print(f"Error- {exc}") 


label = Label(text='Історичні памятки України', font=('Arial', 16, 'bold'))
label.config(bd=10)
label.pack()

kievbutton = tk.Button(text="Історичні пам'ятки Києва")
kievbutton.pack(pady=7)
kievbutton.config(command=attractions.kievAttractions)

kharkivbutton = tk.Button(text="Історичні пам'ятки Харкова")
kharkivbutton.pack(pady=7)
kharkivbutton.config(command=attractions.kharkivAttractions)

lvivbutton = tk.Button(text="Історичні пам'ятки Львова")
lvivbutton.pack(pady=7)
lvivbutton.config(command=attractions.lvivAttractions)

odesabutton = tk.Button(text="Історичні пам'ятки Одеси")
odesabutton.pack(pady=7)
odesabutton.config(command=attractions.odesaAttractions)

zaporizhzhiabutton = tk.Button(text="Історичні пам'ятки Запоріжжя")
zaporizhzhiabutton.pack(pady=7)
zaporizhzhiabutton.config(command=attractions.zaporizhzhiaAttractions)

class info_city():
    def kyiv_kyivopecherskalavra():
        response = requests.get("https://uk.wikipedia.org/wiki/%D0%9A%D0%B8%D1%94%D0%B2%D0%BE-%D0%9F%D0%B5%D1%87%D0%B5%D1%80%D1%81%D1%8C%D0%BA%D0%B0_%D0%BB%D0%B0%D0%B2%D1%80%D0%B0")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup1 = soup.find_all("div", {"class": "mw-content-ltr mw-parser-output"})
            res = soup1[0].find_all("p")
            for i in range(min(num_paragraphs['kiev'][0], len(res))):
                print(res[i].get_text())

    def kyiv_goldengate():
        response = requests.get("https://uk.wikipedia.org/wiki/%D0%97%D0%BE%D0%BB%D0%BE%D1%82%D1%96_%D0%B2%D0%BE%D1%80%D0%BE%D1%82%D0%B0_(%D0%9A%D0%B8%D1%97%D0%B2)")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup1 = soup.find_all("div", {"class": "mw-content-ltr mw-parser-output"})
            res = soup1[0].find_all("p")
            for i in range(min(num_paragraphs['kiev'][1], len(res))):
                print(res[i].get_text())

    def kyiv_monumentmotherlandmotherland():
        response = requests.get("https://uk.wikipedia.org/wiki/%D0%91%D0%B0%D1%82%D1%8C%D0%BA%D1%96%D0%B2%D1%89%D0%B8%D0%BD%D0%B0-%D0%9C%D0%B0%D1%82%D0%B8_(%D0%9A%D0%B8%D1%97%D0%B2)")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup1 = soup.find_all("div", {"class": "mw-content-ltr mw-parser-output"})
            res = soup1[0].find_all("p")
            for i in range(min(num_paragraphs['kiev'][2], len(res))):
                print(res[i].get_text())

    def kharkiv_assumptioncathedral():
        response = requests.get("https://uk.wikipedia.org/wiki/%D0%A1%D0%B2%D1%8F%D1%82%D0%BE-%D0%A3%D1%81%D0%BF%D0%B5%D0%BD%D1%81%D1%8C%D0%BA%D0%B8%D0%B9_%D1%81%D0%BE%D0%B1%D0%BE%D1%80_(%D0%A5%D0%B0%D1%80%D0%BA%D1%96%D0%B2)")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup1 = soup.find_all("div", {"class": "mw-content-ltr mw-parser-output"})
            res = soup1[0].find_all("p")
            for i in range(min(num_paragraphs['kharkiv'][0], len(res))):
                print(res[i].get_text())

    def kharkiv_pokrovskycathedral():
        response = requests.get("https://uk.wikipedia.org/wiki/%D0%9F%D0%BE%D0%BA%D1%80%D0%BE%D0%B2%D1%81%D1%8C%D0%BA%D0%B8%D0%B9_%D1%81%D0%BE%D0%B1%D0%BE%D1%80_(%D0%A5%D0%B0%D1%80%D0%BA%D1%96%D0%B2)")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup1 = soup.find_all("div", {"class": "mw-content-ltr mw-parser-output"})
            res = soup1[0].find_all("p")
            for i in range(min(num_paragraphs['kharkiv'][1], len(res))):
                print(res[i].get_text())

    def kharkiv_derzhprom():
        response = requests.get("https://uk.wikipedia.org/wiki/%D0%94%D0%B5%D1%80%D0%B6%D0%BF%D1%80%D0%BE%D0%BC")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup1 = soup.find_all("div", {"class": "mw-content-ltr mw-parser-output"})
            res = soup1[0].find_all("p")
            for i in range(min(num_paragraphs['kharkiv'][2], len(res))):
                print(res[i].get_text())
    
    def lviv_lvivcityhall():
        response = requests.get("https://uk.wikipedia.org/wiki/%D0%9B%D1%8C%D0%B2%D1%96%D0%B2%D1%81%D1%8C%D0%BA%D0%B0_%D1%80%D0%B0%D1%82%D1%83%D1%88%D0%B0")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup1 = soup.find_all("div", {"class": "mw-content-ltr mw-parser-output"})
            res = soup1[0].find_all("p")
            for i in range(min(num_paragraphs['lviv'][0], len(res))):
                print(res[i].get_text())

    def lviv_archcathedralcathedralofstgeorge():
        response = requests.get("https://uk.wikipedia.org/wiki/%D0%A1%D0%BE%D0%B1%D0%BE%D1%80_%D0%A1%D0%B2%D1%8F%D1%82%D0%BE%D0%B3%D0%BE_%D0%AE%D1%80%D0%B0")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup1 = soup.find_all("div", {"class": "mw-content-ltr mw-parser-output"})
            res = soup1[0].find_all("p")
            for i in range(min(num_paragraphs['lviv'][1], len(res))):
                print(res[i].get_text())

    def lviv_monumenttoastepanbandera():
        response = requests.get("https://uk.wikipedia.org/wiki/%D0%9F%D0%B0%D0%BC%27%D1%8F%D1%82%D0%BD%D0%B8%D0%BA_%D0%A1%D1%82%D0%B5%D0%BF%D0%B0%D0%BD%D0%BE%D0%B2%D1%96_%D0%91%D0%B0%D0%BD%D0%B4%D0%B5%D1%80%D1%96_(%D0%9B%D1%8C%D0%B2%D1%96%D0%B2)")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup1 = soup.find_all("div", {"class": "mw-content-ltr mw-parser-output"})
            res = soup1[0].find_all("p")
            for i in range(min(num_paragraphs['lviv'][2], len(res))):
                print(res[i].get_text())
    
    def odesa_MuseumofWesternandEasternArt():
        response = requests.get("https://uk.wikipedia.org/wiki/%D0%9E%D0%B4%D0%B5%D1%81%D1%8C%D0%BA%D0%B8%D0%B9_%D0%BC%D1%83%D0%B7%D0%B5%D0%B9_%D0%B7%D0%B0%D1%85%D1%96%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE_%D1%96_%D1%81%D1%85%D1%96%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BC%D0%B8%D1%81%D1%82%D0%B5%D1%86%D1%82%D0%B2%D0%B0")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup1 = soup.find_all("div", {"class": "mw-content-ltr mw-parser-output"})
            res = soup1[0].find_all("p")
            for i in range(min(num_paragraphs['odesa'][0], len(res))):
                print(res[i].get_text())

    def odesa_ArtMuseum():
        response = requests.get("https://uk.wikipedia.org/wiki/%D0%9E%D0%B4%D0%B5%D1%81%D1%8C%D0%BA%D0%B8%D0%B9_%D0%BD%D0%B0%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%B8%D0%B9_%D1%85%D1%83%D0%B4%D0%BE%D0%B6%D0%BD%D1%96%D0%B9_%D0%BC%D1%83%D0%B7%D0%B5%D0%B9")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup1 = soup.find_all("div", {"class": "mw-content-ltr mw-parser-output"})
            res = soup1[0].find_all("p")
            for i in range(min(num_paragraphs['odesa'][1], len(res))):
                print(res[i].get_text())

    def odesa_MuseumofModernArt():
        response = requests.get("https://uk.wikipedia.org/wiki/%D0%9C%D1%83%D0%B7%D0%B5%D0%B9_%D1%81%D1%83%D1%87%D0%B0%D1%81%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BC%D0%B8%D1%81%D1%82%D0%B5%D1%86%D1%82%D0%B2%D0%B0_%D0%9E%D0%B4%D0%B5%D1%81%D0%B8")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup1 = soup.find_all("div", {"class": "mw-content-ltr mw-parser-output"})
            res = soup1[0].find_all("p")
            for i in range(min(num_paragraphs['odesa'][2], len(res))):
                print(res[i].get_text())
    
    def zaporizhzhia_DniprovskaHPP():
        response = requests.get("https://uk.wikipedia.org/wiki/%D0%94%D0%BD%D1%96%D0%BF%D1%80%D0%BE%D0%B2%D1%81%D1%8C%D0%BA%D0%B0_%D0%93%D0%95%D0%A1")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup1 = soup.find_all("div", {"class": "mw-content-ltr mw-parser-output"})
            res = soup1[0].find_all("p")
            for i in range(min(num_paragraphs['zaporizhzhia'][0], len(res))):
                print(res[i].get_text())

    def zaporizhzhia_KhortytsiaNationalReserve():
        response = requests.get("https://uk.wikipedia.org/wiki/%D0%9D%D0%B0%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%B8%D0%B9_%D0%B7%D0%B0%D0%BF%D0%BE%D0%B2%D1%96%D0%B4%D0%BD%D0%B8%D0%BA_%C2%AB%D0%A5%D0%BE%D1%80%D1%82%D0%B8%D1%86%D1%8F%C2%BB")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup1 = soup.find_all("div", {"class": "mw-content-ltr mw-parser-output"})
            res = soup1[0].find_all("p")
            for i in range(min(num_paragraphs['zaporizhzhia'][1], len(res))):
                print(res[i].get_text())

    def zaporizhzhia_MuseumoftheHistoryofZaporizhzhyaCossacks():
        response = requests.get("https://uk.wikipedia.org/wiki/%D0%9C%D1%83%D0%B7%D0%B5%D0%B9_%D1%96%D1%81%D1%82%D0%BE%D1%80%D1%96%D1%97_%D0%B7%D0%B0%D0%BF%D0%BE%D1%80%D0%BE%D0%B7%D1%8C%D0%BA%D0%BE%D0%B3%D0%BE_%D0%BA%D0%BE%D0%B7%D0%B0%D1%86%D1%82%D0%B2%D0%B0")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup1 = soup.find_all("div", {"class": "mw-content-ltr mw-parser-output"})
            res = soup1[0].find_all("p")
            for i in range(min(num_paragraphs['zaporizhzhia'][2], len(res))):
                print(res[i].get_text())


root.mainloop()