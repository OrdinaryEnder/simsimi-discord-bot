import aiohttp
import json
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import os


load_dotenv()
language = os.getenv("LANGUAGE")

async def simsimi(content):
    url = f'https://api.simsimi.net/v2/?text={content}&lc={language}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            response = await r.json()
    # print("Respond: " + str(soup)
            return response["success"]
