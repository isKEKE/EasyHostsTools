# _*_ coding: utf-8 _*_
import re
import requests
from githubItem import GithubItem


class GithubIPSpider(object):
    '''爬取Github的最新IP'''
    _api = "https://websites.ipaddress.com/{}"
    def __init__(self):
        self._url = None
        self._response = None
        

    def setHeaders(self) -> dict:
        return {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
        }


    def sendGet(self) -> None:
        '''GET请求'''
        response = requests.get(
            url=self._url,
            headers=self.setHeaders()
        )
        self._response = response


    def parse(self, keyword:str) -> None:
        '''解析响应体'''
        ips = re.findall('''<li>(\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3})</li>''', self._response.text)
        GithubItem.infos[keyword] = ips[0]


    def go(self) -> None:
        '''整合'''
        for keyword in GithubItem.infos:
            self._url = self._api.format(keyword)
            self.sendGet()
            self.parse(keyword)
            print(keyword, "=>", GithubItem.infos.get(keyword))


if __name__ == "__main__":
    GithubIPSpider().go()
