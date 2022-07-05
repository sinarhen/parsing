import aiohttp
import time
from bs4 import BeautifulSoup as bs
import asyncio


headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/103.0.0.0 Safari/537.36'
}

all_pages_html = []


async def gather_data(session, page):
    """Takes response from one page"""
    url = f'https://www.foxtrot.com.ua/uk/shop/mobilnye_telefony_smartfon.html?page={page}'
    async with session.get(url) as resp:
        html = await resp.text()
        print(html)
        return html


async def get_one_page(page):

    async with aiohttp.ClientSession() as session:
        html = await gather_data(session, page)


async def get_many_pages(html):
    for i in range(1, 12):
        soup = bs(html, 'lxml')



loop = asyncio.get_event_loop()
loop.run_until_complete()
