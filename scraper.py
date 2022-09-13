import requests
from contextlib import redirect_stdout
from bs4 import BeautifulSoup
import os
import glob

BASEURL = "http://1000misspenthours.com"
URL = "/general/alphabeticalindex.htm"

page = requests.get(BASEURL + URL)
soup = BeautifulSoup(page.content, "html.parser")


results = soup.find_all('a')

PATH = 'output'
if not os.path.exists(PATH):
    os.makedirs(PATH)
else:
    files = glob.glob(PATH + '/*')
    for f in files:
        os.remove(f)

for i, result in enumerate(results):
    with open(f'output/{i}.txt', 'w') as f:
        with redirect_stdout(f):
            print(result)