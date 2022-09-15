import requests
import utils.file_manager

BASEURL = "http://1000misspenthours.com"
ENCODING = "windows-1252"

def page_save(url, name):
    page = requests.get(BASEURL + url)
    page.encoding = ENCODING

    utils.file_manager.savePage(name, page.text)