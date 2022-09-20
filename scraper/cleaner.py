from bs4 import BeautifulSoup
import utils.file_manager

def page_clean(name):
    pageText = utils.file_manager.getPageText(name)

    soup = BeautifulSoup(pageText, "html.parser")
    print(soup.contents)

    utils.file_manager.savePage(name+ "2.htm", str(soup))