#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File   : C_Scanner.py
@Author : DEADF1SH_CAT
@Date   : 2020/11/18 16:33

Description:

Usage:

'''

import os
import sys
import requests
import socket
import threading

sys.path.append(os.getcwd().replace("plugins",""))
from plugins.Proxy import Proxy

class C_Scanner():
    def __init__(self,url,flag):
        self.host = socket.gethostbyname(url)
        block = self.host.split(".")
        self.base = "{0}.{1}.{2}.".format(block[0],block[1],block[2])
        self.result = []
        if flag:
            self.threads = 100
        else:
            self.threads = 50

    def scan(self,ip):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        try:
            if sock.connect_ex((ip, 80)) == 0:
                print("[+]Host:" + ip + " is opening 80")
                self.result.append(ip)
        except:
            pass

    def threading(self) -> bool:
        '''
        用于celery操作时并发
        '''
        semaphore = threading.BoundedSemaphore(self.threads)
        thread_list = []
        for i in range(1,255):
            ip = self.base + str(i)
            thread = threading.Thread(target=self.scan, args=(ip,))
            thread_list.append(thread)
        for th in thread_list:
            th.start()
        for th in thread_list:
            th.join()
        return True

    @staticmethod
    def AS_lookup(asn):
        proxy = Proxy()
        headers = {
            'User-Agent': proxy.randomUA(),
            'X-Forwarded-For': proxy.randomXFF()
        }
        try:
            #有bug，暂未修复
            r=requests.post("https://hackertarget.com/as-ip-lookup/",data=str(asn),headers=headers)
            res = r.text.split('\n')[1:]
            return res
        except:
            return ("Sorry,网络故障或查询过于频繁...")

if __name__ == "__main__":
    cs = C_Scanner("www.baidu.com",1)
    cs.threading()