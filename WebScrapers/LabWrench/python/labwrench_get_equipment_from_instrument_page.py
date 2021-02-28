import requests
import csv
from bs4 import BeautifulSoup

f = csv.writer(open('equipment_from_instruments_page.csv', 'w'))
f.writerow(['Name'])

instruments_page = requests.get('http://www.labwrench.com/?equipment.list')
soup1 = BeautifulSoup(instruments_page.text, 'html.parser')

alpha_links1 = soup1.find(id='alphaList')
alpha_links1.decompose()
alpha_links2 = soup1.find(id='manufacturerList')
alpha_links2.decompose()
base_links = soup1.find(class_='baseCategory')
base_links.decompose()
other_links = soup1.find(class_='padLeft')
other_links.decompose()

container = soup1.find(class_='menuContainer')
anchor = container.find_all('a')

pages = []

for value in anchor:
    url = 'http://www.labwrench.com' + value.get('href')
    pages.append(url)

    for item in pages:
        page = requests.get(item)
        soup2 = BeautifulSoup(page.text, 'html.parser')

        equipment_list_container = soup2.find(id='equipmentListContainer')
        equipment_content = equipment_list_container.find_all(class_='equipmentContent')

        for paragraph in equipment_content:
            equipment_name = paragraph.a.get_text().strip()
            equipment_link = 'http://www.labwrench.com' + paragraph.a.get('href')

            f.writerow([equipment_name])
