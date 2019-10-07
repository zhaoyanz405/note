import re
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import logging

domain = r'http://www.biqukan.com/'

headers = {'Host': 'www.biqukan.com',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language': 'en-US,en;q=0.5',
           'Accept-Encoding': 'gzip, deflate',
           'Cookie': 'UM_distinctid=16564d3b0c89-06510f2825575b8-386a4645-1fa400-16564d3b0c9323; CNZZDATA1260938422=240533742-1534990457-https%253A%252F%252Fcn.bing.com%252F%7C1535017459; bcolor=; font=; size=; fontcolor=; width=',
           'Connection': 'keep-alive',
           'If-None-Match': "1534944645",
           'Cache-Control': 'max-age=0'}


class UrlNoneException(Exception):
    pass


def get_novel_code_list(url=None):
    """
    获取小说编码列表
    :param url:
    :return:
    """
    if not url:
        raise UrlNoneException('The url must not be NoneType.')

    req = requests.get(url)
    novel_code_list = []
    category_list = []
    bs = BeautifulSoup(req.text)
    a_list = bs.find_all('a')
    for a in a_list:
        href = a.get('href')
        if re.match(r'^/[0-9_]+/$', href):
            novel_code_list.append(href)

        if re.match(r'^/[a-zA-Z]+/$', href):
            category_list.append(href)

    return novel_code_list, category_list


def crawl_directory(url=None):
    """

    :param url:
    :return:
    """
    if not url:
        raise UrlNoneException('The url must not be NoneType.')

    req = requests.get(domain + url)
    bs = BeautifulSoup(req.text)
    a_list = bs.find_all('a')

    directory_list = []
    for a in a_list:
        href = a.get('href')
        if re.match(r'^/[0-9_]+/[0-9]+.html', href):
            directory_list.append(href)

    return directory_list


def crawl_novel(novel_home_page=None):
    """

    :param novel_home_page: 小说主页url
    :return:
    """
    print(domain + novel_home_page)
    if not novel_home_page:
        raise UrlNoneException('The novel homepage must not be NoneType.')

    req = requests.get(domain + novel_home_page, headers=headers)
    bs = BeautifulSoup(req.text)

    #print(req.text)
    div = bs.find_all(id='content')
    pprint(div)
    #pprint(div)
    # for d in div:
    #     print(d)


if __name__ == "__main__":
    crawl_novel(crawl_directory(get_novel_code_list(domain)[0][0])[0])
