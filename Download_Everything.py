"""
Downloads all internal files, 
linked to by any tag's src attribute,
from the home page of the the link
"""

"""
Run this script with caution,  
It downloads everything it comes across with. 
I MEAN EVERYTHING.
"""
import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = 'downloaded' # You can change if you want to
baseUrl = 'https://books.toscrape.com'

def getAbsoluteURL(baseUrl, source):
    if source.startswith('http://www.'):
        url = 'http://{}'.format(source[11:])
    elif source.startswith('http://'):
        url = source
    elif source.startswith('www.'):
        url = source[4:]
        url = 'http://{}'.format(source)
    else:
        url = '{}/{}'.format(baseUrl, source)
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace('www.', '')
    path = path.replace(baseUrl, '')
    if 'http://' in path:
        path = path.split('http://')[1]
    elif 'https://' in path:
        path = path.split('https://')[1]
    path = downloadDirectory+path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    
    return path

html = urlopen('https://books.toscrape.com') # as an example
bs = BeautifulSoup(html, 'html.parser')
downloadList = bs.findAll(src=True) # selects all tags that have the src attribute.

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download['src']) # clean and normalize the urls.
    if fileUrl is not None:
        print(fileUrl)

urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))


