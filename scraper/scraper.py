import requests
from contextlib import redirect_stdout
from bs4 import BeautifulSoup
import os
import glob
import parser
import json
import dataclasses

BASEURL = "http://1000misspenthours.com"
URL = "/general/alphabeticalindex.htm"


with open("data/alpha.htm") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# page = requests.get(BASEURL + URL)
# soup = BeautifulSoup(page.content, "html.parser")
paragraphs = soup.find_all('p')

PATH = 'output'
if not os.path.exists(PATH):
    os.makedirs(PATH)
else:
    files = glob.glob(PATH + '/*')
    for f in files:
        os.remove(f)

movies = [x for x in map(parser.get_movie, paragraphs) if x.name is not None]

print(f'Total movies: {len(movies)}')

with open(f'{PATH}/movies.json', 'w') as f:
    with redirect_stdout(f):
        print(json.dumps(movies, default=lambda n: n.__dict__, indent=4))