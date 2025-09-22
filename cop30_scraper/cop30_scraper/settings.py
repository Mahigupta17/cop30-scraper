BOT_NAME = 'cop30_scraper'

SPIDER_MODULES = ['cop30_scraper.spiders']
NEWSPIDER_MODULE = 'cop30_scraper.spiders'

# Enable your Google Sheets pipeline
ITEM_PIPELINES = {
   "cop30_scraper.pipelines.GoogleSheetsPipeline": 300,
}
