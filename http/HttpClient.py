# -*- coding:gbk -*-
__author__ = 'maclv'

import httplib
import urllib
import urllib2

class agent:

    def get(self,server,path):
        conn = httplib.HTTPConnection(server)
        conn.request("GET", path)
        r1 = conn.getresponse()
        body = r1.read()
        conn.close()
        if r1.status == 200:
            print r1.status, r1.reason
            print r1.getheader("set-cookie")
            self.cookie=r1.getheader("set-cookie")

    def post(self,server,path,parameters):

        params = urllib.urlencode({'dname':'麦轲',
                           'phone':'',
                           'psw':'mac8.666'
                           });

        headers = {"Content-Type":"application/x-www-form-urlencoded",
                    "Connection":"Keep-Alive",
                    "Referer":"http://"+server+'/',
                    "Cookie":self.cookie
                    }

        conn = httplib.HTTPConnection(server)
        conn.request(method="POST",url="/login.htm?",body=params,headers=headers)
        response = conn.getresponse()
        body = response.read()
        conn.close()
        print response.status, response.reason
        print headers
        print response.getheaders()
        #print body

    def get2(self,server,path):
            headers = {"Content-Type":"application/x-www-form-urlencoded",
                    "Connection":"Keep-Alive",
                    "Referer":"http://"+server+'/',
                    "Cookie":self.cookie
                    }

            conn = httplib.HTTPConnection(server)
            conn.request(method="get",url=path,headers=headers)
            response = conn.getresponse()
            body = response.read()
            conn.close()
            print response.status, response.reason
            print headers
            print response.getheaders()
            print body

