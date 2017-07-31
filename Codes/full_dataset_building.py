#
#   @author      : SRvSaha
#   Filename     : full_dataset_building.py
#   Timestamp    : 16:52 31-July-2017 (Monday)
#   Description  : Script to Scrape whole website kitchenstories.io for
#                  creating dataset of cooking domain
#

"""
Scraper for whole website to prepare full dataset.
"""


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

##############################
##     GLOBAL VARIABLES     ##
##############################

BASE = URL = "https://kitchenstories.io/en/recipes"
URLS = set()
COUNT = 1


def get_valid_page(URL):
    '''
    The method takes in URL as the parameter, request the page, get its content
    if possible (Code 200) and then create a BeautifulSoup object and return it
    '''
    r = requests.get(URL)
    if r.status_code == 200:
        return BeautifulSoup(r.content, 'lxml')
    else:
        return None

###################################################################


def recursive_crawler(URL):
    '''
    Recursive Crawler crawls all the URLs that are available and adds them
    to a set so that there is no duplicate URL
    '''
    flag = False
    soup = get_valid_page(URL)
    if soup:
        for url in get_valid_page(URL).find_all('a'):
            if url.get('href').startswith("/en/recipes/"):
                URLS.add(urljoin(BASE, url.get('href')))
            elif url.get('href').startswith("?page"):
                flag = True
                next_page_url = url.get('href')
    if flag:
        URL = urljoin(BASE, next_page_url)
        global COUNT
        COUNT += 1
        recursive_crawler(URL)
        return COUNT

print("Depth Crawled:", recursive_crawler(URL))

###############################################################

f = open("../Data/full_dataset.txt", 'w')
for first, URL in enumerate(URLS):
    counter = 0
    output = []
    soup = get_valid_page(URL)
    if soup:
        for item in soup.find_all('p'):
            if str(item).startswith("<p class=\"text\">"):
                counter += 1
                text = ' '.join((item.get_text()).split('\n'))
                output.append('I' + str(first + 1) + '.' +
                              str(counter) + '\t' + text + '\n')
        f.write('R' + str(first + 1) + '\t' +
                URL[URL.rfind('/') + 1:] + '\t' + str(counter) + '\n')
        f.writelines(output)
        print(first + 1)

f.close()
print("Operation Successful in file: Data/full_dataset.txt")
