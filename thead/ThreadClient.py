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
    print "线程 "+str(no)+ " 结束！"
    #thread.exit_thread() #这一行是不需要的，“When the function returns, the thread silently exits. ”

def threadtest1():
    #函数式：调用thread模块中的start_new_thread()函数来产生新线程,这里返回的t1,t2 是int型
    t1=thread.start_new_thread(task, (1,1))
    t2=thread.start_new_thread(task, (2,2))
    time.sleep(20)
    



    #基于thread模块的start_new_thread方法已经不推荐使用了，在IDLE中这段代码可以正确运行，在其他环境下可能会报如下错误,sys.excepthook is missing
    #原因：启动线程之后，须确保主线程等待所有子线程返回结果后再退出，如果主线程比子线程早结束，无论其子线程是否是后台线程，都将会中断，抛出这个异常 。
    #所以这里在主线程中加入sleep


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

    #如果t1,t2两个线程都启动起来了，并且活着，我们就call join 等待线程结束，20秒是超时时间
    if t1.is_alive and t2.is_alive:
        t1.join(20)
        t2.join(20)

    print "==over=="

if __name__ == "__main__":
    print "== 测试 python multi threads=="
    threadtest1()
    #threadtest2()
