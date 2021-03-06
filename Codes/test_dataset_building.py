#
#   @author      : SRvSaha
#   Filename     : test_beatiful.py
#   Timestamp    : 15:45 31-July-2017 (Monday)
#   Description  : Script to extract 10 Similar Foods' Preparation Method from
#                  kitchenstories.io for buidling prototype ontology
#

"""
Script for building dataset for Testing the Prototype Discourse Model
"""


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

URL = "https://kitchenstories.io/en/recipes/american-apple-pie"


def get_url(URL):
    r = requests.get(URL)
    if r.status_code == 200:
        return BeautifulSoup(r.content, 'lxml')

BASE = "http://kitchenstories.io"
URLS = set()

soup = get_url(URL)
for url in soup.find_all('a'):
    if str(url.get('href')).startswith('/en/recipes/'):
        URLS.add(urljoin(BASE, url.get('href')))

URLS_ = URLS.copy()

flag = False
while len(URLS) < 10:
    for url in URLS_:
        soup = get_url(url)
        for page in soup.find_all('a'):
            if page.get('href').startswith('/en/recipes/') and len(URLS) != 10:
                URLS.add(urljoin(BASE, page.get('href')))
                if len(URLS) == 10:
                    flag = True
                    break
        if flag:
            break

f = open("../Data/test_dataset.txt", 'w')
for first, URL in enumerate(URLS):
    counter = 0
    output = []
    r = requests.get(URL)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'lxml')
        for item in soup.find_all('p'):
            if str(item).startswith("<p class=\"text\">"):
                counter += 1
                output.append('I' + str(first + 1) + '.' +
                              str(counter) + '\t' + item.get_text() + '\n')
        f.write('R' + str(first + 1) + '\t' +
                URL[URL.rfind('/') + 1:] + '\t' + str(counter) + '\n')
        f.writelines(output)
f.close()
print("Operation Successful in file: Data/test_dataset.txt")
