import requests
from bs4 import BeautifulSoup
import csv

url = 'https://zakup.kbtu.kz/zakupki/sposobom-zaprosa-cenovyh-predlozheniy'

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
# }
list_title, deadline, status, htp, organizers = [], [], [], [], []
base_url = 'https://zakup.kbtu.kz/'

header = ['НАЗВАНИЕ', 'ДАТА ОКАНЧАНИЕ', 'СТАТУС']

for page in range(1,40):
    r = requests.get(f'https://zakup.kbtu.kz/zakupki/sposobom-zaprosa-cenovyh-predlozheniy&page={page}')

    soup = BeautifulSoup(r.content, features='html5lib')

    target = soup.find_all('div', class_='card-body')
    links = soup.find_all('p', class_='card-text')
    p = soup.find_all('div', class_="card-body")

    for cont in target:
        list_title.append(cont.a.text.strip())
    for cont_a in soup.select("p.card-text span"):
        status.append(cont_a.text)
    for strong in soup.select("p.card-text strong"):
        deadline.append(strong.text)

with open('Zalog.csv' , 'w', encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header)

    for x in range(len(list_title)):
        
        csv_writer.writerow([list_title[x], deadline[x], status[x]])
        

csv_file.close()