#!/usr/bin/env python
# coding=utf-8

__author__ = 'feiyu'

#配置log模块

import os
import logging



LOG_PATH = os.path.abspath(os.path.join(__file__,'..'))

logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename=os.path.join(LOG_PATH, 'chatroom.log'),
        filemode='a'
    )












