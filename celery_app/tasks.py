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
    print("-"*21 + "Start WebFinger Matching" + "-"*21)
    for i in port:
        host = url + ":" + str(i)
        print(host)
    #host = url
    try:
        WFinger = WebFinger(host, flag)
        if WFinger.threading():
            print("[+] " + WFinger.host +" use:")
            result = ""
            for j in WFinger.result:
                result += j + "  "
            print("[+] fofa_banner: " + result)
    except Exception as e:
        raise(e)

    print("-"*23 + "End WebFinger Matching" + "-"*21)
    return WFinger.result

@app.task
def CDN_WAF_Finger_T():
    print("-"*19 + "Start CDN/WAF Finger Matching" + "-"*18)
    print("-"*20 + "End CDN/WAF Finger Matching" + "-"*19)

@app.task
def SubdomainScan_T():
    print("-"*22 + "Start Subdomain Scan" + "-"*22)
    print("-"*23 + "End Subdomain Scan" + "-"*23)

@app.task
def Whois_Scan_T():
    print("-"*24 + "Start Whois Scan" + "-"*24)
    print("-"*25 + "End Whois Scan" + "-"*25)
    
@app.task
def CIDR_Scan_T():
    print("-"*24 + "Start CIDR Scan" + "-"*25)
    print("-"*25 + "End CIDR Scan" + "-"*26)

@app.task
def GSIL_Scan_T():
    print("-"*24 + "Start GSIL Scan" + "-"*25)
    print("-"*25 + "End GSIL Scan" + "-"*26)