from typing import Iterable
import scrapy
from scrapy.http import Request
from bookscraper.items import BookItem
import random
from urllib.parse import urlencode

API_KEY = 'e27e65ab-6033-4402-b5a8-e8762c9e0eee'

def get_proxy_url(url):
    payload = {'api_key': API_KEY, 'url':url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com", 'proxy.scrapeops.io']
    start_urls = ["https://books.toscrape.com/"]


    # A list of random user agents,
    # This is not effecient for a large scale website.
    # user_agents_list = [
    #     'Mozilla/5.0 (Macintosh; PPC Mac OS X 10 11_0) AppleWebKit/533.1 (KHTML, like Gecko) Chrome/59.0.811.0 Safari/533.1'
    #     'Opera/8.18.(Windows NT 6.2; tt-RU) Presto/2.9.169 Version/11.00'
    #     'Opera/8.40.(X11; Linux i686; ka-GE) Presto/2.9.176 Version/11.00'
    #     'Opera/9.42.(X11; Linux x86_64; sw-KE) Presto/2.9.180 Version/12.00'
    #     'Mozilla/5.0 (Macintosh; PPC Mac OS X 10 5_1 rv:6.0; cy-GB) AppleWebKit/533.45.2 (KHTML, like Gecko) Version/5.0.3 Safari/533.45.2'
    #     'Opera/8.17.(X11; Linux x86_64; crh-UA) Presto/2.9.161 Version/11.00'
    #     'Mozilla/5.0 (compatible; MSIE 5.0; Windows NT 5.1; Trident/3.1)'
    #     'Mozilla/5.0 (Android 3.1; Mobile; rv:55.0) Gecko/55.0 Firefox/55.0'
    #     'Mozilla/5.0 (compatible; MSIE 9.0; Windows CE; Trident/5.0)'
    #     'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10 11_9; rv:1.9.4.20) Gecko/2019-07-26 10:00:35 Firefox/9.0'
    # ]

    # Its takes the 1st url and passes it to the proxy provider(scrapeops.io)
    # It might still work without it but the start url will not be passed to the proxy
    def start_requests(self):
        yield scrapy.Request(url=get_proxy_url(self.start_urls[0]), callback=self.parse)

    def parse(self, response):
        books = response.css('article.product_pod')
        
        for book in books:
            relative_url = book.css('h3 a ::attr(href)').get()
            if 'catalogue/' in relative_url:
                book_url = 'https://books.toscrape.com/' + relative_url
            else:
                book_url = 'https://books.toscrape.com/catalogue/' + relative_url
                # Pick a random user agent and insert it to the header on the callback whenever a request is sent.
                # headers={"User-Agent": self.user_agents_list[random.randint(0, len(self.user_agents_list)-1)]}
            yield scrapy.Request(url=get_proxy_url(book_url), callback=self.parse_book_page)
        
        next_page = response.css('li.next a ::attr(href)').get()
        if next_page is not None:
            if 'catalogue/' in next_page:
                next_page_url = 'https://books.toscrape.com/' + next_page
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
                # Pick a random user agent and insert it to the header on the callback whenever a request is sent.
            yield scrapy.Request(url=get_proxy_url(next_page_url), callback=self.parse)


    def parse_book_page(self, response):
        table_rows = response.css("table tr")
        book_item = BookItem()
        
        
        book_item['url'] = response.url,
        book_item['title'] = response.css('.product_main h1::text').get(),
        book_item['upc'] = table_rows[0].css("td ::text").get()
        book_item['product_type'] = table_rows[1].css("td ::text").get(),
        book_item['price_excl_tax'] = table_rows[2].css("td ::text").get(),
        book_item['price_incl_tax'] = table_rows[3].css("td ::text").get(),
        book_item['tax'] = table_rows[4].css("td ::text").get(),
        book_item['availability'] = table_rows[5].css("td ::text").get(),
        book_item['reviews'] = table_rows[6].css("td ::text").get(),
        book_item['stars'] = response.css('p.star-rating').attrib['class'],
        book_item['category'] = response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
        book_item['description'] = response.xpath("//div[@id='product_description']/following-sibling::p/text()").get(),
        book_item['price'] = response.css('p.price_color ::text').get(),       
        
        yield book_item