# Takes two args from the user
from sys import argv
from bs4 import BeautifulSoup
import requests


def what_links_here(article):
    """
    Returns a list of all Wikipedia articles that this article links to.
    """
    articles = []
    html_page = requests.get(
        f'https://en.wikipedia.org/w/index.php?title=Special:WhatLinksHere/'
        f'{article}&namespace=0&limit=500&hideredirs=1&hidetrans=1')
    soup = BeautifulSoup(html_page.text, "lxml")
    for span in soup.findAll('span', {'class': 'mw-whatlinkshere-tools'}):
        link = span.contents[1]['href']
        index = link.find('target=')
        articles.append(link[index + len('target='):])


scriptName, firstArg, secondArg = argv
rootPage = "https://en.wikipedia.org/wiki/"
startPage = rootPage + firstArg.replace(" ","_")
endPage = rootPage + secondArg.replace(" ","_")
print("Executing {0}! Your starting page is {1} and your end location is {2}".format(scriptName,startPage,endPage))

what_links_here(rootPage)
