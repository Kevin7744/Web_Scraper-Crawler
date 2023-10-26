from bs4 import BeautifulSoup
from urllib.request import urlopen
import pprint
import re
import random
import datetime
# with open ("indx.html", "r") as html_file:
#  readFile = BeautifulSoup(html_file, "html.parser")  
# pTags = readFile.find_all("p")[0]

# pprint.pprint(pTags.string)
pp = pprint.PrettyPrinter(depth=6)

# def getTitle(url):
#         html = urlopen('https://en/wikipedia.org{}'.format(url))
#         readFIle = BeautifulSoup(html, "html.parser")
#         title = readFIle.title.string
#         return title

# def getLinks(file):
#     links = []
#     text = []
#     try:
#         html_file = open(file, "r")
#         readFile = BeautifulSoup(html_file, 'html.parser')
#     except Exception as error:
#         print("There seems to be a problem somewhere with the file")
#     for link in readFile.find('div', {'class': 'box'}).find_all('a', {'class': 'itm'}):
#         if 'href' in link.attrs:
#             links.append(link.attrs['href'])
#             for link in links:
#                 pp = pprint.PrettyPrinter(depth=6)
#                 pp.pprint(links)
#     for text in readFile.find('div', {'class': 'box'}).find_all('span', {'class':'text'}):
#         if 'text' in text.attrs:
#             text.append(text.attr['text'])
#             for text in text:
#                 pp = pprint.PrettyPrinter(depth=6)
#                 pp.pprint(text)
#     return (links, text)

# title = getTitle('/wiki/Kevin_Bacon')
# pp.pprint(title)

# links = getLinks('jumia.html')
pages = set()
# random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen('https://en.wikipedia.org{}'.format(articleUrl))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                pp.pprint(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks('')
# links = getLinks('/wiki/Kevin_Bacon')
# while len(links) > 0:
#     newArticle = links[random.randint(0, len(links)-1)].attrs['href']
#     pp.pprint(newArticle)
#     links = getLinks(newArticle)

