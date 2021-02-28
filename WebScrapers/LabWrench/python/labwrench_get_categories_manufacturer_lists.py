import requests
import csv
from bs4 import BeautifulSoup

f = csv.writer(open('categories_manufacturer_lists.csv', 'w'))
f.writerow(['Name', 'Link'])

# Collect and parse first page
page = requests.get('http://www.labwrench.com/?equipment.list')
# page = requests.get('http://www.labwrench.com/?equipment.list/?equipment.list/Tab/categoryList/FilterLetter/A/')
# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

alpha_links = soup.find(id='alphaList')
alpha_links.decompose()


# Pull all text from the letterBlock div
container = soup.find(class_='tabContentContainer')

# Pull text from all instances of <a> tag within letterBlock div
anchor = container.find_all('a')

# Create for loop to print out all artists' names
# for term in letter_block_terms:
#     print(term.prettify())

# Use .contents to pull out the <a> tag’s children
for term in anchor:
    names = term.contents[0]
    links = 'http://www.labwrench.com' + term.get('href')
#    print(names.strip())
#    print(links.strip())

    f.writerow([names.strip(), links])



