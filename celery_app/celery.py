#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: DEADF1SH_CAT
@File: celery.py
@About: 
'''

from __future__ import absolute_import
from celery import Celery

app = Celery('celery_app')
app.config_from_object('celery_app.config')

if __name__ == '__main__':
    app.start()