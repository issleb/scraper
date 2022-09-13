from dataclasses import dataclass
import re

def get_movie(tag):
    year = _get_year(tag)

    movie = Movie()
    movie.year = year

    return movie


def _get_year(text):
    regex = r"/A> \((....)"
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
