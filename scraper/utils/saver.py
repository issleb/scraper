import requests
from bs4 import BeautifulSoup
import utils.file_manager

BASEURL = "http://1000misspenthours.com"
ENCODING = "windows-1252"

def page_save(url, name):
    page = requests.get(BASEURL + url)
    page.encoding = ENCODING
    soup = BeautifulSoup(page.text, "html.parser")

    utils.file_manager.savePage(name, str(soup))