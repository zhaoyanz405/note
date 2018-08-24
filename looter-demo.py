#! /usr/bin/python
# -*- coding: utf-8 -*-
# @author: Zhao Yan
# @datetime: 8/24/18 10:11 AM
import re
import time
import looter
import asyncio
from pprint import pprint

domain = r'http://www.biqukan.com/'

category_list = [domain]
novel_url_list = []
finished_category_list = []
finished_novel_url_list = []


async def crawl(route_url):
    if not route_url:
        return ''

    tree = await looter.async_fetch(domain + route_url if domain not in route_url else route_url)
    lines = tree.css("div[id='content']::text").extract()
    for line in lines:
        # line = line.replace('\xa0', '')
        print(line)


async def crawl_directory(novel_url):
    tree = await looter.async_fetch(domain + novel_url if domain not in novel_url else novel_url)
    title = tree.css("h2::text").extract()[0]
    a_list = tree.css('a')

    chapters_dict = dict()
    for a in a_list:
        href = a.css("a::attr(href)").extract()[0]
        if re.match(r'^/[0-9_]+/[0-9]+.html$', href):
            name = a.css("a::text").extract()[0]
            chapters_dict[name] = href
            print(title)
            print(name)
            await crawl(href)


async def crawl_novel_list(url):
    global category_list, finished_category_list, novel_url_list

    tree = await looter.async_fetch(domain + url if domain not in url else url)
    href_list = tree.css('a::attr(href)').extract()
    for href in href_list:
        if re.match(r'^/[a-zA-Z]+/$', href):
            if href not in category_list and href not in finished_category_list:
                category_list.append(href)

        if re.match(r'^/[0-9_]+/$', href):
            novel_url_list.append(href)

    try:
        category_list.remove(url)
        finished_category_list.append(url)
    except Exception as e:
        print(e)
        print(href_list)
        print('url:' + url)
        raise e


async def crawl_until_finish():
    global category_list, novel_url_list
    category_list = list(set(category_list))
    while category_list:
        pprint('now ,category_list is : ')
        pprint(category_list)
        await crawl_novel_list(category_list[0])
        if not category_list:
            time.sleep(1 * 60)

    for novel_url in list(set(novel_url_list)):
        await crawl_directory(novel_url)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([crawl_directory('/16_16379/')]))
