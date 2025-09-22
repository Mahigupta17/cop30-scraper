import scrapy

class Cop30ScraperItem(scrapy.Item):
    scheduled = scrapy.Field()
    time_location = scrapy.Field()
    organizer = scrapy.Field()
    title_theme_speakers = scrapy.Field()
    source_url = scrapy.Field()
    last_updated = scrapy.Field()
