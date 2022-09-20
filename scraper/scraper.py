from bs4 import BeautifulSoup
import parser
import json
import utils.file_manager
import utils.saver
import argparse

def save():
    #utils.file_manager.clearOutput()

    #utils.saver.page_save("/general/alphabeticalindex.htm", "alpha.htm")
    movies = utils.file_manager.getMovies("data/movies.json")

    for movie in movies:
        utils.saver.page_save(movie.link, movie.name + ".htm")

def parse():
    with open("data/alpha.htm") as fp:
        soup = BeautifulSoup(fp, "html.parser")

        paragraphs = soup.find_all('p')
        movies = [x for x in map(parser.get_movie, paragraphs) if x.name is not None]
        print(f'Total movies: {len(movies)}')

        utils.file_manager.savePage('movies.json', json.dumps(movies, default=lambda n: n.__dict__, indent=4)) 

def clean():
    pass


argParser = argparse.ArgumentParser()
argParser.add_argument("mode", help="(S)ave or (P)arse", choices=["S", "P", "C"])
args = argParser.parse_args()

if args.mode == "S":
    save()
elif args.mode == "P":
    parse()
elif args.mode == "C":
    clean()    

## need python 3.10
# match args.mode:
#     case "S":
#         save()
#     case "M":
#         parse()
#     case _:
#         # default