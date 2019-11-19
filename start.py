#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: DEADF1SH_CAT
@File: start.py
@About: 
'''

import os

def start():
    os.system('start powershell -Command ^&{celery -A celery_app worker -l info -P eventlet}')
    #os.system('start cmd /k celery -A celery_app worker -l info -P eventlet')
    for i in range(10):
        os.system('start powershell -Command ^&{celery -A celery_app worker -l info -P eventlet}')

if __name__ == '__main__':
    start()