#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File   : Proxy.py
@Author : DEADF1SH_CAT
@Date   : 2020/11/18 11:19

Description:

Usage:

'''

from faker import Factory
from faker.providers import internet
from faker.providers import user_agent

class Proxy():
    def __init__(self):
        self.proxylist = []
        self.fake = Factory.create()

    def randomXFF(self):
        self.fake.add_provider(internet)

        return self.fake.ipv4_private()

    def randomUA(self):
        self.fake.add_provider(user_agent)

        return self.fake.user_agent()

if __name__ == "__main__":
    proxy = Proxy()
    print(proxy.randomXFF())
    print(proxy.randomUA())