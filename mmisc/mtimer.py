# -*- coding:utf-8 -*-
__author__ = 'lvkun.lk'

import time, datetime


def showtime():
    #打印当前时间，time和datetime的区别之一是 datetime可以得到“毫秒级”的时间
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    #print datetime.datetime.now()
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))