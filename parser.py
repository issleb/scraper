from dataclasses import dataclass
from dataclasses_json import dataclass_json
import re

def get_movie(tag):
    
    title = _get_title(tag)
    year = _get_year(tag)
    link = _get_link(tag)
    rating = _get_rating(tag)

    movie = Movie(title=title, link=link, year=year, rating=rating)
    return movie

def _get_title(text):
    regex = r'>([^<]*)</a>'
    result = _search(regex, text)
    return result

def _get_year(text):
    regex = r'/a> \((....)'
    result = _search(regex, text)
    return result

def _get_link(text):
    regex = r'f="([^"]*)">'
    result = _search(regex, text)
    return result    

def _get_rating(text):
    regex = r'/a> \(....\) ([^<]*)' 
    result = _search(regex, text)
    return result        


def _search(regex, text):
    result = re.search(regex, text)

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