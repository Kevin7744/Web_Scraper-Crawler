from bs4 import BeautifulSoup
import pprint
# with open ("indx.html", "r") as html_file:
#  readFile = BeautifulSoup(html_file, "html.parser")  
# pTags = readFile.find_all("p")[0]

# pprint.pprint(pTags.string)

def getTitle(file):
    try:
        html_file = open (file, "r")
    except FileNotFoundError as fileError:
        print("Check file or file not found")
    try:
        readFIle = BeautifulSoup(html_file, "html.parser")
        title = readFIle.title.string
    except AttributeError as error:
        return None 
    return title

def get_P_Tags(file):
    try:
        html_file = open (file, "r")
    except FileNotFoundError as fileError:
        print("Check file or file not found")
    try:
        readFIle = BeautifulSoup(html_file, "html.parser")
        pTags = readFIle.find_all("p", string="Kevin Kipkoech")
    except AttributeError as error:
        print("There are no p tags in the page, or there is just a problem")
    return pTags

def getDivs(file):
    try:
        html_file = open (file, "r")
    except FileNotFoundError as fileError:
        print("Check file or file not found")
    try:
        readFIle = BeautifulSoup(html_file, "html.parser")
        divs = readFIle.find('div', {"class":"sidebar"}).find_all('div', {"class": "contact"})
    except AttributeError as error:
        print("There was problem getting the divs")
    return divs
def getTable(file):
    try:
        html_file = open(file, "r")
    except FileNotFoundError as fileError:
        print("Check the file or file not found")
    try:
        readFile = BeautifulSoup(html_file, "html.parser")
        table = readFile.find('div', {"class": "table-container"}).find_all('tr')
    except AttributeError as error:
        print("There was a problem getting the table data")
    return  table


title = getTitle("Index.html")
if title == None:
    print("Title not found, please check the file again")
else:
    print(title)


pTags = get_P_Tags("Index.html")
if pTags == None:
    print("There is a problem getting the p tags")
else:
    print(pTags)


divs = getDivs("Index.html")
if divs == None:
    print("Div not found, Please check prompt again")
else:
    print(divs)

table = getTable("Index.html")
if table == None:
    print("Table not found, Please check prompt again")
else:
    print(table)
    

