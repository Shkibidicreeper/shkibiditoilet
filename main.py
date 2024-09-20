import requests
from bs4 import BeautifulSoup

url = 'https://www.tktarelka.ru/cinema/schedule/'

response = requests.get(url)

fullfilms = ['название фильма']
fullsubtitle = ['описание фильма']

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')
    
    
    films = soup.find_all('div', class_='title')
    

    for film in films:
        print(film.text.strip())
        fullfilms.append(film.text.strip())

        subtitles = soup.find_all('div', class_='subtitle')
    
    print("\n")
    for subtitle in subtitles:
        print(subtitle.text.strip())
        fullsubtitle.append(subtitle.text.strip())

else:
    print(f'Ошибка при подключении к сайту: {response.status_code}')
    print(fullfilms)
    print(fullsubtitle)
    
    #данные из масива перекинуть в csv файл залить в гитхаб там все доделать
# Открытие файла для записи
with open("csvfailik.csv", mode='w', encoding='utf-8') as csvfile:
    csvfile.write('Название, Описание')

    for item in range(len(fullfilms)):
        line = f"{fullfilms[item]},{fullfilms[item]}\n"
        csvfile.write(line)
print()