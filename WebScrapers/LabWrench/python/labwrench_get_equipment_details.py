import requests
import csv
from bs4 import BeautifulSoup

f = csv.writer(open('equipment_details.csv', 'w'))
f.writerow(['Name', 'Description'])

page = requests.get('http://www.labwrench.com/?equipment.view/equipmentNo/23673/Postnova/AF2000-MultiFlow/')
soup = BeautifulSoup(page.text, 'html.parser')

equip_view = soup.find(id='equipViewTabContents')
description_div = equip_view.find(id='lnkDescriptionText')
header1 = description_div.find_all('h3')
paragraph = description_div.find_all(class_='descriptionContent')

for text in header1:
    equipment_name = text.contents[0]

for text in paragraph:
    description = text.contents[0]

    f.writerow([equipment_name.strip(), description.strip()])



