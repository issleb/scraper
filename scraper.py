import requests
from contextlib import redirect_stdout
from bs4 import BeautifulSoup

BASEURL = "http://1000misspenthours.com"
URL = "/general/alphabeticalindex.htm"

page = requests.get(BASEURL + URL)
soup = BeautifulSoup(page.content, "html.parser")


results = soup.find_all('a')

for i, result in enumerate(results):
    with open(f'output/{i}.txt', 'w') as f:
        with redirect_stdout(f):
            print(result)