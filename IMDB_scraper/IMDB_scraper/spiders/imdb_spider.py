# to run
# scrapy crawl imdb_spider -o movies.csv

import scrapy

class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'
    
    start_urls = ['https://www.imdb.com/title/tt1839578/']
    
parse(self, response):

parse_full_credits(self, response):

parse_actor_page(self, response):


