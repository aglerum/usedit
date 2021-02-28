import requests
import csv
from bs4 import BeautifulSoup

f = csv.writer(open('category_description.csv', 'w'))
f.writerow(['Title', 'Link'])

page = requests.get('http://www.labwrench.com/?equipment.list/categoryNo/3076/categoryName/accessories/')
soup = BeautifulSoup(page.text, 'html.parser')

community_options = soup.find(class_='communityOptions')
community_options.decompose()

equipment_list_container = soup.find(id='equipmentListContainer')
equipment_content = equipment_list_container.find_all(class_='equipmentContent')

for paragraph in equipment_content:
    equipment_title = paragraph.a.get_text().strip()
    equipment_link = 'http://www.labwrench.com' + paragraph.a.get('href')
    f.writerow([equipment_title, equipment_link])

#     print(equipment_title)
#     print(equipment_link)



