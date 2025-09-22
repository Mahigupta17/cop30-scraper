import gspread
from google.oauth2.service_account import Credentials

class GoogleSheetsPipeline:
    def open_spider(self, spider):
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = Credentials.from_service_account_file(
            "C:\Users\mahig\OneDrive\Desktop\scrapper\sheet-scraper-bot-472309-de1c2aa26ac3.json",
            scopes=scopes
        )
        client = gspread.authorize(creds)
        self.sheet = client.open("COP30 Events Tracker").sheet1

    def process_item(self, item, spider):
        self.sheet.append_row([
            item.get("scheduled"),
            item.get("time_location"),
            item.get("organizer"),
            item.get("title_theme_speakers"),
            item.get("source_url"),
            item.get("last_updated")
        ])
        return item
