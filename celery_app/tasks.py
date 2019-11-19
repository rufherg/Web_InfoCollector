#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: DEADF1SH_CAT
@File: tasks.py
@About: 
'''

from __future__ import absolute_import

from celery import Celery
from celery import group

from celery_app.celery import app
from plugins.PortScanner import *
from plugins.WebFinger import *

@app.task
def PortScanner_T(url, start, end, flag):
    PScan = PortScanner(url, start, end, flag)
    print("-"*25 + "Start PortScanner" + "-"*25)
    if PScan.threading():
        print("-"*27 + "End PortScanner" + "-"*25)
    return PScan.result

@app.task
def WebFinger_T(port, url, flag):
    print("-"*20 + "Start WebFinger Matching" + "-"*20)
    for i in port:
        host = url + ":" + str(i)
        print(host)
    #host = url
    try:
        WFinger = WebFinger(host, flag)
        if WFinger.thread():
            print("[+] " + WFinger.host +" use:")
            result = ""
            for j in WFinger.finger:
                result += j + "  "
            print("[+] fofa_banner: " + result)
    except:
        pass
    print("-"*22 + "End WebFinger Matching" + "-"*20)
