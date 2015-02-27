# -*- coding:gbk -*-
__author__ = 'maclv'

import thread

def foo0(arg):
    print "call "+ str(foo0.__name__) +", "+ str(arg[0])

def foo1(args):
    print "call foo1 " + str(args[0]) + ", "+str(args[1])

def foo2(args):
    print "call foo2 " + str(args[0]) + ", "+str(args[1])+", "+str(args[2])

foo3=lambda arg1,arg2: arg1+arg2
# ���ֲ���д���е�lambda���� print ��return ���������Ҳ����д


def run(fun,*args): #һ��*���ڲ���ǰ��������������ܿɱ�����Ĳ�����run��fun��2��3��5��...��
    fun(args)

def run2(fun,**args): #����**���ڲ���ǰ��������������ܿɱ�����Ĳ���,�����ֵ�ķ�ʽ����run2��fun��key1=v1��key2=v2��key3=v3��...��
    print "\ncall fun: "+str(fun.__name__)
    for x in args:
        print x + ": " + str(args[x])

if __name__ == "__main__":
    print "���� ����funcition ��ط��� ����"
    run(foo0,1)
    run(foo1,1,2)
    run(foo2,1,2,3)

    run2(foo0, key1="v1", key2="v2")







    """  ====Reference====
    filter(function, sequence)����sequence�е�item����ִ��function(item)����ִ�н��ΪTrue��item���һ��List/String/Tuple��ȡ����sequence�����ͣ����أ�
    >>> def f(x): return x % 2 != 0 and x % 3 != 0
    >>> filter(f, range(2, 25))
    [5, 7, 11, 13, 17, 19, 23]
    >>> def f(x): return x != 'a'
    >>> filter(f, "abcdef")
    'bcdef'


    map(function, sequence) ����sequence�е�item����ִ��function(item)����ִ�н�����һ��List���أ�
    >>> def cube(x): return x*x*x
    >>> map(cube, range(1, 11))
    [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    >>> def cube(x) : return x + x
    ...
    >>> map(cube , "abcde")
    ['aa', 'bb', 'cc', 'dd', 'ee']
    ����mapҲ֧�ֶ��sequence�����Ҫ��functionҲ֧����Ӧ�����Ĳ������룺
    >>> def add(x, y): return x+y
    >>> map(add, range(8), range(8))
    [0, 2, 4, 6, 8, 10, 12, 14]


    reduce(function, sequence, starting_value)����sequence�е�item˳���������function�������starting_value����������Ϊ��ʼֵ���ã��������������List��ͣ�
    >>> def add(x,y): return x + y
    >>> reduce(add, range(1, 11))
    55 ��ע��1+2+3+4+5+6+7+8+9+10��
    >>> reduce(add, range(1, 11), 20)
    75 ��ע��1+2+3+4+5+6+7+8+9+10+20��


    lambda������Python֧��һ����Ȥ���﷨������������ٶ��嵥�е���С������������C�����еĺ꣬��Щ����lambda�ĺ������Ǵ�LISP�������ģ����������κ���Ҫ�����ĵط���
    >>> g = lambda x: x * 2
    >>> g(3)
    6
    >>> (lambda x: x * 2)(3)
    6


    ����Ҳ���԰�filter map reduce ��lambda��������ã������Ϳ��Լ򵥵�д��һ�С�
    ����
    kmpathes = filter(lambda kmpath: kmpath,
    map(lambda kmpath: string.strip(kmpath),
    string.split(l, ':')))
    �������鷳����ʵ��������������������һ�����ǳ����š�
    �� l �е�����Ԫ����':'���ָ�ó�һ���б�������б��ÿһ��Ԫ�����ַ���strip���γ�һ���б�������б��ÿһ��Ԫ����ֱ�ӷ��ز���(����ط����Լ��Ϲ�����������)�����ջ��һ���ַ�����':'�ָ���б��б��е�ÿһ���ַ���������strip�������Զ������ַ������ˡ�
    """


