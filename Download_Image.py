# uses urllib library to download images from a remote url

from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

# using pythonscraping.com as an example
html = urlopen('http://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
imageLocation = bs.find('a', {'id': 'logo'}).find('img')['src']
urlretrieve(imageLocation, '/images/logo.jpg')
