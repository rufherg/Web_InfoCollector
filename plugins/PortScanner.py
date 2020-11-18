#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: DEADF1SH_CAT
@File: Port_Scanner.py
@About: 
'''

import socket
import concurrent.futures
import datetime
import argparse
import sys,re
import threading

class PortScanner():
    def __init__(self, host, start_port, end_port, flag):
        self.host = socket.gethostbyname(host)
        self.Sport = int(start_port)
        self.Eport = int(end_port)
        self.result = []
        if flag:
            self.threads = 100
        else:
            self.threads = 50

    def run(self):
        print("-"*25 + "Start PortScanner" + "-"*25)
        if self.thread():
            print("-"*27 + "End PortScanner" + "-"*25)

    def scan(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        try:
            if sock.connect_ex((self.host, port)) == 0:
                print("[+]Host:" + self.host + " is opening " + str(port))
                self.result.append(port)
        except:
            pass

    def thread(self) -> bool:
        threadpool = concurrent.futures.ThreadPoolExecutor(max_workers = self.threads)
        futures = (threadpool.submit(self.scan, port) for port in range(self.Sport, self.Eport + 1))
        for i in concurrent.futures.as_completed(futures):
            pass
        return True

    def threading(self) -> bool:
        '''
        用于celery操作时并发
        '''
        semaphore = threading.BoundedSemaphore(self.threads)
        thread_list = []
        for port in range(self.Sport, self.Eport + 1):
            thread = threading.Thread(target=self.scan, args=(port,))
            thread_list.append(thread)
        for th in thread_list:
            th.start()
        for th in thread_list:
            th.join()
        return True

if __name__ == "__main__":
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
            start_time = datetime.datetime.now()
            portscanner = PortScanner(url, start, end, flag)
            portscanner.run()
            spend_time = (datetime.datetime.now() - start_time).seconds
            print("Total time: " + str(spend_time) + " seconds")
        except:
            print("Args ERROR!")
            exit()