"""
Stores all pages on wikipedia that have a "Bacon number"
(The numbe of links between it and the page for Kevin Bacon)
of 6 or less
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql
from random import shuffle


conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    passwd='kevin4747',
    charset='utf8'
)
cur = conn.cursor()
cur.execute('USE sixdegrees')

def insertPageIfNotExists(url):
    cur.execute('SELECT * FROM pages WHERE url = %s', (url))
    if cur.rowcount == 0:
        cur.execute('INSERT INTO pages (url) VALUES (%s)', (url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]

def loadPage():
    cur.execute('SELECT * FROM pages')
    pages = [row[1] for row in cur.fetchall()]
    return pages

def insertLink(fromPageId, topageId):
    cur.execute('SELECT * FROM links WHERE fromPageId = %s '
                'AND topageId = %s', (int(fromPageId), int(topageId)))
    if cur.rowcount == 0:
        cur.execute('INSERT INTO links (fromPageId, topageId) VALUES (%s, %s)',
                    (int(fromPageId), int(topageId)))
        conn.commit()

def getLinks(pageUrl, recursionLevel, pages):
    if recursionLevel > 4:
        return
    
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    links = bs.findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    links = [link.attrs['href'] for link in links]

    for link in links:
        insertLink(pageId, insertPageIfNotExists(link))
        if link not in pages:
            #add a new page
            pages.append(link)
            getLinks(link, recursionLevel+1, pages)

getLinks('/wiki/William_Ruto', 0, loadPage())
cur.close()
conn.close