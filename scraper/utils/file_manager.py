import os
from contextlib import redirect_stdout
import glob

OUTPUT_PATH = 'output'

def clearOutput():
    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)
    else:
        files = glob.glob(OUTPUT_PATH + '/*')
        for f in files:
            os.remove(f)

def savePage(name, text):
    with open(f'{OUTPUT_PATH}/{name}', 'w') as f:
        with redirect_stdout(f):
            print(text)
