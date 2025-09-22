import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define scope
scope = ["https://www.googleapis.com/auth/spreadsheets", 
         "https://www.googleapis.com/auth/drive"]

# Authenticate
creds = ServiceAccountCredentials.from_json_keyfile_name(
    "sheet-scraper-bot-472309-de1c2aa26ac3.json", scope
)
client = gspread.authorize(creds)

# Open spreadsheet by name
spreadsheet = client.open("COP30 Events Tracker")  # make sure this matches EXACTLY
sheet = spreadsheet.sheet1  # first tab

# Print current contents
print("Before:", sheet.get_all_values())

# Update cell
sheet.update_cell(1, 1, "Hello COP30!")

# Print again
print("After:", sheet.get_all_values())
