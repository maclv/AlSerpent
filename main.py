# -*- coding:utf-8 -*-
__author__ = 'lvkun.lk'

from mmisc import initconf,mtimer

from http import HttpClient

config_file_path="global_setting.ini"

def info():
    print """::KLV:: Tool set of Mac Lv @Alipay from 2014::
    [USAGE]
    main.py  -h                         #print this help info   [打印帮助信息]
    main.py  -a  <algorithm>            #runing the algorithm   [运行指定算法]

    ==options==
    <algorith>
    """

if __name__ == "__main__":
    print "==START=="
    #info()
    #mtimer.showtime()
    agent=HttpClient.agent()
    agent.get("alimovie.taobao.net","/login.htm")
    agent.post("alimovie.taobao.net","/login.htm",'')
    agent.get2("alimovie.taobao.net","/movie_detail.htm?id=1361")
    print "==End=="


