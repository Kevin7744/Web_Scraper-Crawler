from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii', 'ignore')

dataFile = StringIO(data)
csvreader = csv.reader(dataFile)
for row in csvreader:
    print(row)
