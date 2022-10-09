import requests
import bs4

import os

from .utils.proxy import StandardHTTPProxyRotator

class Asura(object):
    def __init__(self, url, proxyRotator = StandardHTTPProxyRotator):
        self.url = url.strip("/")
        self.slug = os.path.split(self.url)[1]

        self.proxyRotator = proxyRotator()
    
    def extract(self, soup):        
        status = soup.find("div", attrs={"class":"imptdt"}).i.text

        chapters = soup.find("ul", attrs={"class":"clstyle"}).find_all("li") # in descending order
        
        latest_chapter = chapters[0]
        latest_chapter_num = int(latest_chapter['data-num'])
        latest_chapter_name = latest_chapter.find("span", attrs={"class": "chapternum"}).text
        latest_chapter_date = latest_chapter.find("span", attrs={"class": "chapterdate"}).text
        latest_chapter_url = latest_chapter.find("a")['href']

        result = {
            "status": status,
            "latest_chapter": latest_chapter_num,
            "title": latest_chapter_name,
            "last_updated": latest_chapter_date,
            "url": latest_chapter_url,
            "slug": self.slug
        }
        return result

    def get(self):
        r = requests.get(self.url, proxies=next(self.proxyRotator))
        soup = bs4.BeautifulSoup(r.text, "html.parser")
        result = self.extract(soup)
        return result
    
class AsyncAsura(object):
    def __init__(self, url, proxyRotator = StandardHTTPProxyRotator):
        self.url = url.strip("/")
        self.slug = os.path.split(self.url)[1]

        self.proxyRotator = proxyRotator() # bu async uyumlu degil hata verebilir
    
    async def extract(self, response_text):
        soup = bs4.BeautifulSoup(response_text, "html.parser")
        status = soup.find("div", attrs={"class":"imptdt"}).i.text

        chapters = soup.find("ul", attrs={"class":"clstyle"}).find_all("li") # in descending order
        
        latest_chapter = chapters[0]
        latest_chapter_num = int(latest_chapter['data-num'])
        latest_chapter_name = latest_chapter.find("span", attrs={"class": "chapternum"}).text
        latest_chapter_date = latest_chapter.find("span", attrs={"class": "chapterdate"}).text
        latest_chapter_url = latest_chapter.find("a")['href']

        result = {
            "status": status,
            "latest_chapter": latest_chapter_num,
            "title": latest_chapter_name,
            "last_updated": latest_chapter_date,
            "url": latest_chapter_url,
            "slug": self.slug
        }

        return result

    async def get(self, session):
        proxy = next(self.proxyRotator)
        async with session.get(self.url, proxy=proxy['http']) as response:
            response_text = await response.text()
            result = await self.extract(response_text)
        
        return result