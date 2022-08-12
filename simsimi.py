import cloudscraper
import json
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import os

scraper = cloudscraper.create_scraper()
load_dotenv()
language = os.getenv("LANGUAGE")

def simsimi(content):
    url = f'https://api.simsimi.net/v2/?text={content}&lc={language}'
    response = scraper.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    # print("Respond: " + str(soup))
    text = json.loads(soup.text)
    return text["success"]
