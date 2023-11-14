# from bs4 import BeautifulSoup
# import re


# with open("jumia.html", "r") as file:
#     html = BeautifulSoup(file, "html.parser")


# def getTitle(html_file):
#     title = html_file.find("title")
#     return title.string

# def getProductLink(html_file):
#     link = html_file.find("link", {'rel':'canonical'}) 
#     return link

# def getProductInfo_and_Price(html_file):
#     info = html_file.find("main").find_all('div', {'class': '-hr -mtxs -pvs'})
#     return info

# def getOtherProducts(html_file):
#     header = html_file.header
#     link = header.find('div', {'class': 'box'})
#     internalLinks = []
#     # Find all links that begin with a '/'
#     for link in link.find_all('a', href=re.compile('^(/|.*'')')):
#         if link.attrs['href'] is not None:
#             if link.attrs['href'] not in internalLinks:
#                 if(link.attrs['href'].startswith('/')):
#                     internalLinks.append(link.attrs['href'])
#                 else:
#                     internalLinks.append(link.attrs['href'])
#     name_fixed = header.find_all('span', {'class': 'text'})
#     return internalLinks, name_fixed



# product = getTitle(html), 
# producLink = getProductLink(html)
# price = getProductInfo_and_Price(html)
# others = getOtherProducts(html)
# print(product)
# print()
# print(producLink)
# print()
# print(price)
# print()
# print(others)

from bs4 import BeautifulSoup
import re

with open("jumia.html", "r") as file:
    html = BeautifulSoup(file, "html.parser")

def getTitle(html_file):
    title = html_file.find("title")
    return title.string

def getProductInfo_and_Price(html_file):
    product_name = html_file.find('main').find_all('h1', {'class': '-fs20 -pts -pbxs'})[0].text.strip()
    info = html_file.find("main").find_all('div', {'class': '-hr -mtxs -pvs'})
    info_text = ""
    for div in info:
        price = div.find('span', {'dir': 'ltr'}).text.strip()
        original_price = div.find_all('span', {'dir': 'ltr'})[1].text.strip()  # Get the second span element
        discount_percentage = div.find('span', {'data-disc': True})['data-disc']
        info_text += f"Product: {product_name}\nPrice: {price}\nOriginal Price: {original_price}\nDiscount Percentage: {discount_percentage}\n\n"
    return info_text


def getOtherProducts(html_file):
    header = html_file.header
    link = header.find('div', {'class': 'box'})
    internalLinks = []
    other_products_text = ""
    for a in link.find_all('a', href=re.compile('^(/|.*'')')):
        href = a.get('href')
        text = a.find('span', {'class': 'text'}).text.strip()
        other_products_text += f"Link: {href}\nName: {text}\n\n"
    return other_products_text

title = getTitle(html)
product_info_and_price = getProductInfo_and_Price(html)
other_products = getOtherProducts(html)

print("Title of the page:")
print(title)
print("\nProduct Info and Price:")
print(product_info_and_price)
print("\nOther Products:")
print(other_products)
