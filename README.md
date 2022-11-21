# misspent-scraper

## Installation
- `pip3 install -r scraper/requirements.txt`

## Running

- `python scraper/scraper.py <switch>`
- `python scraper/scraper.py --help` for help

- (S)ave will download all the reviews listed in data/movies.json. You can also uncomment a line and download the movie index.
- (P)arse will parse the downloaded movie index into JSON.
- (C)lean is a work in progress to parse individual movie reviews.

## Testing

-`pytest tests`