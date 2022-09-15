from dataclasses import dataclass
from dataclasses_json import dataclass_json
import re

def get_movie(tag):
    tag = str(tag)
    if "<table" in tag.lower():
        return Movie()
    
    title = _get_title(tag)
    year = _get_year(tag)
    link = _get_link(tag)
    rating = _get_rating(tag)
    name = _get_name(tag)

    movie = Movie(title=title, link=link, year=year, rating=rating, name=name)

    if movie.title is None:
        print(f"Warning: Empty title on {tag}")
    if movie.link is None:
        print(f"Warning: Empty link on {tag}")        
    if movie.year is None:
        print(f"Warning: Empty year on {tag}")
    if movie.rating is None:
        print(f"Warning: Empty rating on {tag}")        

    return movie

def _get_title(text):
    regex = r'>([^<]*)</a>'
    result = _search(regex, text)
    return result

def _get_year(text):
    regex = r'/a> \(([^\)]*)'
    result = _search(regex, text)
    return result

def _get_link(text):
    regex = r'f="([^"]*)">'
    result = _search(regex, text)
    return result    

def _get_rating(text):
    regex = r'/a> \([^\)]*\) ([^<]*)' 
    result = _search(regex, text)
    return result

def _get_name(text):
    regex = r'reviews[^/]+/([^\.]*).h' 
    result = _search(regex, text)
    return result    


def _search(regex, text):
    result = re.search(regex, text, re.IGNORECASE)

    if not result:
        return

    return result.group(1)    

@dataclass_json
@dataclass
class Movie:
    title: str = None
    year: str = None
    link: str = None
    rating: str = None
    name: str = None