#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File   : CDN_WAF_Finger.py
@Author : DEADF1SH_CAT
@Date   : 2020/11/18 11:17

Description:

Usage:

'''

import os
import sys
import requests
import urllib3
import json

sys.path.append(os.getcwd().replace("plugins",""))
from plugins.Proxy import Proxy

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class CDN_WAF_Finger():
    def __init__(self,url):
        self.url = "http://" + url
        self.header = self.getHeaders()

    def getHeaders(self):
        proxy = Proxy()
        headers = {
            'User-Agent': proxy.randomUA(),
            'X-Forwarded-For': proxy.randomXFF()
        }
        try:
            req = requests.get(self.url, headers=headers, timeout=15, verify=False)
            return req.headers
        except Exception as e:
            try:
                req = requests.head(self.url, headers=headers, timeout=15, verify=False)
                return req.headers
            except:
                return {}

    def useCDN(self):
        try:
            key = False
            cdn_headers = [
                'X-CDN',
                'via',
                'x-cache',
                'x-swift-cachetime',
                'X-Cache-Lookup',
                'X-Via',
                'Via',
                'X-Via-CDN',
                'X-Cdn',
                'X-Cache',
                'CDN-Cache',
                'CDN-Server',
                'X-Cdn-Srv',
                'Cdn',
                'CDN',
                'Cache-Control',
                'X-Cache-Error',
                'X-Upper-Cache',
                "X-Cacheable",
                'X-Cacheable-status',
                'X-Status',
                'X-DNS',
                'X-Proxy',
                'CacheStatus',
                'X-Fastcgi-Cache',
                'X-Backend',
                'X-PingBack',
                'X-Executed-By',
                'X-Front',
                'X-Server',
                'CDN-Node',
                'X-Rack-Cache',
                'X-Request-Id',
                'X-Runtime',
            ]
            for cdn_head in cdn_headers:
                if cdn_head in self.header:
                    key = True
            return key
        except Exception as e:
            print(e)

        return False

    def useCDN_WAF(self):
        key = []
        self.json = json.load(open(os.getcwd().replace("plugins","") + "./database/cdnwaf.json",encoding='utf-8'))
        try:
            sdict = self.header
            for skey in sdict:
                for dkey in self.json:
                    if skey in self.json[dkey]:
                        if self.json[dkey][skey] in sdict[skey]:
                            key.append(dkey)
        except Exception as e:
            print(e)
        self.result = list(set(key))

        return self.result

if __name__ == "__main__":
    finger = CDN_WAF_Finger("www.baidu.com")
    print(finger.useCDN_WAF())
