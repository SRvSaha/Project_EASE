import requests
from bs4 import BeautifulSoup


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

URLS = ['http://kitchenstories.io/en/recipes/creamy-quinoa-porridge', 'http://kitchenstories.io/en/recipes/speculaas-cookies', 'http://kitchenstories.io/en/recipes/bavarian-apple-fritters',
        'http://kitchenstories.io/en/recipes/marbled-coffee-cake', 'http://kitchenstories.io/en/recipes/dark-n-stormy', 'http://kitchenstories.io/en/recipes/paleo-seed-bread', 'http://kitchenstories.io/en/recipes/colorful-chiffonade-salad']

f = open("../Data/corner_case_test_dataset.txt", 'w')
steps = 0   # This is to keep track of the corner case where recipes has no
            # description of how to do, but a one liner. We need to remove it
            # and match the index accordingly. So this acts as normalizer.
for first, URL in enumerate(URLS):
    counter = 0
    output = []
    soup = get_valid_page(URL)
    if soup:
        for item in soup.find_all('p'):
            if str(item).startswith("<p class=\"text\">"):
                counter += 1
                text = ' '.join((item.get_text()).split('\n'))
                output.append('I' + str(first - steps + 1) + '.' +
                              str(counter) + '\t' + text + '\n')
        if counter > 1:
            first -= steps
            f.write('R' + str(first + 1) + '\t' +
                    URL[URL.rfind('/') + 1:] + '\t' + str(counter) + '\n')
            f.writelines(output)
        else:
            steps += 1
        print(first + 1)

f.close()
print("Operation Successful in file: Data/corner_case_test_dataset.txt")
