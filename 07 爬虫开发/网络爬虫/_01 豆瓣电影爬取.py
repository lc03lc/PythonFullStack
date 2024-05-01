import asyncio

import aiohttp
from lxml import etree

INDEX_URL = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit={}&page_start={}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'
}
LIMIT = 20
PAGE_START = 0


async def execute(url, session):
    async with session.get(url=url, headers=headers) as response:
        return await response.json()


async def parse_index(url, session):
    async with session.get(url=url, headers=headers) as response:
        html = await response.text()
        tree = etree.HTML(html)
        title = tree.xpath('//*[@id="content"]/h1/span[1]/text()')
        print(title)


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [execute(INDEX_URL.format(LIMIT, page), session) for page in range(0, 100, 20)]
        results = await asyncio.gather(*tasks)
        index = [parse_index(t.get('url'), session) for j in results for t in j.get('subjects')]
        title = await asyncio.gather(*index)
        print(title)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
