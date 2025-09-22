import scrapy
from datetime import datetime
from cop30_scraper.items import Cop30ScraperItem

class EventsSpider(scrapy.Spider):
    name = "events"
    start_urls = [
        "https://unfccc.int/process-and-meetings/conferences/side-events-and-exhibits?utm_source=chatgpt.com" 
        "https://seors.unfccc.int/?utm_source=chatgpt.com" 
        "https://cop30.br/en/brazilian-presidency/calendar?utm_source=chatgpt.com"
        "https://www.nature.org/en-us/what-we-do/our-priorities/tackle-climate-change/climate-change-stories/cop-climate-change-conference/?utm_source=chatgpt.com"
        "https://oceanpavilion-cop.org/?utm_source=chatgpt.com" 
        "https://ngocongo.org/event/cop30-unfccc-timelines-for-the-selection-process-for-a-side-event-and-or-an-exhibit/?utm_source=chatgpt.com" # <-- replace with a real event URL
    ]

    def parse(self, response):
        # Example: extract event blocks
        for event in response.css("div.event-card"):  
            item = Cop30ScraperItem()
            item['scheduled'] = event.css("span.date::text").get()
            item['time_location'] = event.css("span.location::text").get()
            item['organizer'] = event.css("span.organizer::text").get()
            item['title_theme_speakers'] = event.css("h3.title::text").get()
            item['source_url'] = response.url
            item['last_updated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            yield item
