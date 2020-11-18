#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File   : Subdomain.py
@Author : DEADF1SH_CAT
@Date   : 2020/11/18 20:56

Description:

Usage:

'''

import os
import sys
import requests
import re
import urllib3
import threading

from bs4 import BeautifulSoup

sys.path.append(os.getcwd().replace("plugins",""))
from plugins.Proxy import Proxy

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Subdomain():
    def __init__(self,url,flag):
        self.domain = url
        self.result = []
        if flag:
            self.threads = 100
        else:
            self.threads = 50

    def get_count(self):
        url = "https://tool.chinaz.com/subdomain/?domain={}&page=1".format(self.domain)
        data = requests.get(url, headers=self.set_header(), timeout=3, verify=False)
        content = data.text
        soup = BeautifulSoup(content, "lxml")
        string = soup.findAll("span",attrs={"class":"col-gray02"})[0].string
        count = re.findall('\d+',string)[0]
        
        return count

    def get_data(self,page):
        result = []
        url = "https://tool.chinaz.com/subdomain/?domain={}&page={}".format(self.domain,page)
        data = requests.get(url, headers=self.set_header(), timeout=3, verify=False)
        content = data.text
        soup = BeautifulSoup(content, "lxml")
        data_group = soup.find_all("div",attrs={"class":"w23-0 subdomain"})
        for data in data_group:
            result.append(data.a.string)
            self.result.append(data.a.string)

        return result

    def set_header(self):
        proxy = Proxy()
        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'User-Agent':proxy.randomUA(),
            'Upgrade-Insecure-Requests':'1',
            'Connection':'keep-alive',
            'Cache-Control':'max-age=0',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'zh-CN,zh;q=0.8',
            "Referer": "https://www.baidu.com/link?url=Ni7wOsdwUuz50m1no12V0q3QtNYXbNgXoybY9SUqoKG",
            'Cookie':"PHPSESSID=gljsd5c3ei5n813roo4878q203"
        }

        return headers

    def threading(self) -> bool:
        '''
        用于celery操作时并发
        '''
        semaphore = threading.BoundedSemaphore(self.threads)
        thread_list = []
        for page in range(1, int(self.get_count()) + 1):
            thread = threading.Thread(target=self.get_data, args=(page,))
            thread_list.append(thread)
        for th in thread_list:
            th.start()
        for th in thread_list:
            th.join()

        return True


if __name__ == "__main__":
    sub = Subdomain("www.meituan.com",1)
    sub.threading()