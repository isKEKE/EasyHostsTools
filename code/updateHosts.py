# _*_ coding: utf-8 _*_
import os
import re
from requests.exceptions import RequestException
from githubItem import GithubItem
from githubIPSpider import GithubIPSpider
from settings import HOSTS_PATH

class UpdateHosts(object):
    '''更新HOSTS文件'''
    @staticmethod
    def exists() -> None:
        '''判断HOSTS路径是否正确'''
        if HOSTS_PATH is None:
            raise AttributeError("请填写`./settings.py`文件中`HOSTS_PATH`属性.")

        if not os.path.exists(HOSTS_PATH):
            raise AttributeError("路径下`HOSTS`文件不存在.")


    @staticmethod
    def reload() -> None:
        '''重载'''
        content = open(HOSTS_PATH, "r").read()
        for keyword, value in GithubItem.infos.items():
            repl = f'''{value} {keyword}'''
            if keyword in content:
                pattern = '''\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} %s''' % keyword
                content = re.sub(pattern, repl, content)
            else:
                content += f"\n{repl}"
        # 重新写入
        open(HOSTS_PATH, "w").write(content)
        os.system("ipconfig /flushdns")


    @classmethod
    def go(cls)-> int:
        '''更新'''
        # 判断路径下HOSTS文件是否存在
        cls.exists()

        # 获取最新IP数据
        try:
            GithubIPSpider().go()
        except RequestException:
            return -1
        else:
            if input("是否更新(y/n) ").lower() != "y":
                return -1

            # 重载更新
            cls.reload()
        return 0


    @staticmethod
    def pause() -> None:
        os.system("pause")

if __name__ == "__main__":
    UpdateHosts.go()