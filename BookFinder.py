# WEB SCRAPING ATTEMPT NUMBER 67786855365
# source: BookFinder.com
# input: ISBN integer (preferably no whitespaces, dashes, etc.)
# output: variables containing author, title and year

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import Request

from database_holder import new_book

barcode = open("barcode_results.txt",'r')
ISBN = barcode.readline().rstrip("\n")  # <- will be substituted with actual output from Machine Learning
site = 'https://www.bookfinder.com/search/?isbn=' + ISBN + '&mode=isbn&st=sr&ac=qr'

# padding to avoid HTTP 4003 error
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site, headers=hdr)
url = urlopen(req)

# Create BeautifulSoup object
bs = BeautifulSoup(url, 'html.parser')

# -------------------------------------------------------
# In case BookFinder.com doesn't have info on one of the entries


def unavailable(columnName, string):
    if columnName == None:
        print(string + ' is unavailable')
        columnName = 'N/A'
    else:
        columnName = columnName.get_text()
        print(columnName)

    return columnName
# -------------------------------------------------------


# Search segment, based on html architecture of BookFinder.com
title = bs.find('div', {'class': 'attributes'}).find('span', {'itemprop': 'name'})
title = unavailable(title, 'Title')

author = bs.find('div', {'class': 'attributes'}).find('span', {'itemprop': 'author'})
author = unavailable(author, 'Author')

year = bs.find('div', {'class': 'attributes'}).find('span', {'itemprop': 'publisher'})
year = unavailable(year, 'Year')

new_book(ISBN, title, author, year, "default")


