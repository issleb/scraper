from contextlib import redirect_stdout
from bs4 import BeautifulSoup
import parser
import json
import utils.file_manager

with open("data/alpha.htm") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

paragraphs = soup.find_all('p')
movies = [x for x in map(parser.get_movie, paragraphs) if x.name is not None]
print(f'Total movies: {len(movies)}')

# utils.file_manager.clearOutput()
utils.file_manager.savePage('movies.json', json.dumps(movies, default=lambda n: n.__dict__, indent=4))