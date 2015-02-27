# -*- coding:gbk -*-
__author__ = 'maclv'

import time
import thread
from threading import  Thread


def task(no, interval):
    cnt=0
    while cnt<10:
        print 'Thread:(%d) Time:%s\n'%(no, time.ctime())
        time.sleep(interval)
        cnt+=1
    print "�߳� "+str(no)+ " ������"
    #thread.exit_thread() #��һ���ǲ���Ҫ�ģ���When the function returns, the thread silently exits. ��

def threadtest1():
    #����ʽ������threadģ���е�start_new_thread()�������������߳�,���ﷵ�ص�t1,t2 ��int��
    t1=thread.start_new_thread(task, (1,1))
    t2=thread.start_new_thread(task, (2,2))
    time.sleep(20)
    



    #����threadģ���start_new_thread�����Ѿ����Ƽ�ʹ���ˣ���IDLE����δ��������ȷ���У������������¿��ܻᱨ���´���,sys.excepthook is missing
    #ԭ�������߳�֮����ȷ�����̵߳ȴ��������̷߳��ؽ�������˳���������̱߳����߳�����������������߳��Ƿ��Ǻ�̨�̣߳��������жϣ��׳�����쳣 ��
    #�������������߳��м���sleep


class threadclass(Thread):
    """docstring for MyThread"""
    def __init__(self,no,interval):
        super(threadclass,self).__init__()
        self.no=no
        self.interval=interval

    def run(self):
        task(self.no,self.interval)


def threadtest2():
    t1=threadclass(1,1)
    t2=threadclass(2,2)

    t1.start()
    t2.start()

    #���t1,t2�����̶߳����������ˣ����һ��ţ����Ǿ�call join �ȴ��߳̽�����20���ǳ�ʱʱ��
    if t1.is_alive and t2.is_alive:
        t1.join(20)
        t2.join(20)

    print "==over=="

if __name__ == "__main__":
    print "== ���� python multi threads=="
    threadtest1()
    #threadtest2()
