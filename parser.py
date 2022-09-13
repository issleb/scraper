from dataclasses import dataclass
import re

def get_movie(tag):
    title = _get_title(tag)
    year = _get_year(tag)
    link = _get_link(tag)
    rating = _get_rating(tag)

    movie = Movie()
    movie.title = title
    movie.link = link
    movie.year = year
    movie.rating = rating

    return movie

def _get_title(text):
    regex = r'>([^<]*)</A>'
    result = _search(regex, text)
    return result

def _get_year(text):
    regex = r'/A> \((....)'
    result = _search(regex, text)
    return result

def _get_link(text):
    regex = r'F="([^"]*)">'
    result = _search(regex, text)
    return result    

def _get_rating(text):
    regex = r'/A> \(....\) ([^<]*)' 
    result = _search(regex, text)
    return result        


def _search(regex, text):
    result = re.search(regex, text)

    if not result:
        return

    return result.group(1)    


@dataclass
class Movie:
    title: str = None
    year: str = None
    link: str = None
    rating: str = None
