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

page = requests.get(BASEURL + URL)
soup = BeautifulSoup(page.content, "html.parser")
paragraphs = soup.find_all('p')

PATH = 'output'
if not os.path.exists(PATH):
    os.makedirs(PATH)
else:
    files = glob.glob(PATH + '/*')
    for f in files:
        os.remove(f)

movies = list(map(lambda n: parser.get_movie(str(n)), paragraphs))

with open(f'output/movies.json', 'w') as f:
    with redirect_stdout(f):
        print(json.dumps(movies, default=lambda n: n.__dict__ ))