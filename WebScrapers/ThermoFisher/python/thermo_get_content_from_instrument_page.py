import requests
import csv
from bs4 import BeautifulSoup

f = csv.writer(open('thermo_content.csv', 'w'))
f.writerow(['Name'])

instruments_page = requests.get('https://www.thermofisher.com/us/en/home/order/lab-instruments-equipment.html')
soup1 = BeautifulSoup(instruments_page.text, 'html.parser')

container = soup1.find(class_='parsys_column')
list_container = container.find(class_='listcontainer')
anchor = list_container.find('a')

pages = []

for value in anchor:
    url = anchor.get('href')
    pages.append(url)

    for item in pages:
        page = requests.get(item)
        soup2 = BeautifulSoup(page.text, 'html.parser')

        equipment_details_container1 = soup2.find(class_='result-container')
        equipment_details_container2 = equipment_details_container1.find(class_='result-container')

# Good up to here
        for details in equipment_details_container2.div.result:
            equipment_name = details.find('h2').a.get_text().strip()
            # equipment_link = paragraph.a.get('href')
            # equipment_description = paragraph.find('h2').get_text().strip()

            print(equipment_name)


