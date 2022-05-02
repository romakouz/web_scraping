# to run
# scrapy crawl imdb_spider -o movies.csv

import scrapy

class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'
    
    start_urls = ['https://www.imdb.com/title/tt0106145/']
    
    def parse(self, response):
        cast_crew_page = "fullcredits"
        #cast_link = response.css("a[href*='fullcredits']"::attr(href)")
        cast_url = response.urljoin(cast_crew_page)
        yield scrapy.Request(cast_url, callback = self.parse_full_credits)
    def parse_full_credits(self, response):
        cast_list = [a.attrib["href"] for a in response.css("td.primary_photo a")]
        for actor in cast_list:
            actor_url = "https://www.imdb.com" + actor
            yield scrapy.Request(actor_url, callback = self.parse_actor_page)
    def parse_actor_page(self, response):
        actor_name = response.css("h1.header span.itemprop::text").get()
        for movie in response.css("div.filmo-row"):
            if "actor" in movie.css("::attr(id)").get():
                yield {
                    "actor" : actor_name,
                    "movie_or_TV_name" : movie.css("a::text").get()
                }
