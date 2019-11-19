#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: DEADF1SH_CAT
@File: Web_Info.py
@About: 
'''

import argparse
import os,sys,re
import datetime,time

from celery_app.tasks import *

def init():
    os.system('start powershell -Command ^&{celery -A celery_app worker -l info -P eventlet}')
    #os.system('start cmd /k celery -A celery_app worker -l info -P eventlet')  --CMD
    #os.system('gnome-terminal -x bash -c "celery -A celery_app worker -l info") --Ubuntu(未测试)
    #os.system("gnome-terminal -e 'celery -A celery_app worker -l info'") --CentOS(未测试)

def run(url, start, end, flag):
    result = (PortScanner_T.s(url, start, end, flag) | WebFinger_T.s(url, flag))()
    #result = PortScanner_T.delay(url, start, end, flag)
    print(result.get())

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.argv.append('-h')

    parser = argparse.ArgumentParser(description='Port Scanner',add_help=True)
    parser.add_argument('-u','--url',default=None,help='目标URL',type=str)
    parser.add_argument('-p','--port',default="1-65535",help='待扫描的端口范围(默认1-65535)')
    parser.add_argument('-m','--max',default=None,help='最高线程模式(max=100)',action="store_true")
    args = parser.parse_args()

    if args.max:
        flag = 1
    else:
        flag = 0

    if args.url:
        try:
            url = re.sub('(http|https)://',"",args.url, re.I)
            try:
                port = args.port.split("-")
                if len(port) > 2:
                    print("Args for Port ERROR!")
                    exit()
                else:
                    start = port[0]
                    end = port[1]
            except:
                start = args.port
                end = args.port
            init()
            start_time = datetime.datetime.now()
            run(url, start, end, flag)
            spend_time = (datetime.datetime.now() - start_time).seconds
            print("Total time: " + str(spend_time) + " seconds")
        except:
            print("Args ERROR!")
            exit()