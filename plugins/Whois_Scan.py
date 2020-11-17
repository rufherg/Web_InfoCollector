#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File   : Whois_Scan.py
@Author : DEADF1SH_CAT
@Date   : 2020/11/17 21:43

Description:

Usage:

'''

import socket
import json
from ipwhois import IPWhois

class Whois_Scan():
    def __init__(self,url):
        self.obj = IPWhois(socket.gethostbyname(url))
        self.result = {}

    def IP_rdap(self):
        result = self.obj.lookup_rdap()
        return result

    def IP_asn(self):
        result = self.obj.lookup_rdap(depth=1)
        print(json.dumps("AS"+result["asn"]))


    def IP_whois(self):
        result = self.obj.lookup_rdap()
        print(json.dumps(result,indent=4))


    def run(self):
        result = self.IP_rdap()
        print("asn: AS" + result["asn"])
        print("asn_cidr: " + result["asn_cidr"])
        print("asn_registry: " + result["asn_registry"])
        print("asn_country_code: " + result["asn_country_code"])
        print("asn_description: " + result["asn_description"])

if __name__ == '__main__':
    Whois_Scan(socket.gethostbyname('www.baidu.com')).run()