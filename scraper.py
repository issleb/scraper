import requests
from contextlib import redirect_stdout

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# print(page.text)


with open('output/out.txt', 'w') as f:
    with redirect_stdout(f):
        print(page.text)