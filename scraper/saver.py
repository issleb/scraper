import requests
import utils.file_manager

BASEURL = "http://1000misspenthours.com"
URL = "/general/alphabeticalindex.htm"

page = requests.get(BASEURL + URL)
page.encoding = 'windows-1252'

# utils.file_manager.clearOutput()
utils.file_manager.savePage('alpha.htm', page.text)