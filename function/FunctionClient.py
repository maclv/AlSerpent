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
# 发现不能写多行的lambda而且 print 和return 这样的语句也不能写


def run(fun,*args): #一个*号在参数前代表这个函数接受可变数码的参数，run（fun，2，3，5，...）
    fun(args)

def run2(fun,**args): #两个**号在参数前代表这个函数接受可变数码的参数,并以字典的方式来，run2（fun，key1=v1，key2=v2，key3=v3，...）
    print "\ncall fun: "+str(fun.__name__)
    for x in args:
        print x + ": " + str(args[x])

if __name__ == "__main__":
    print "＝＝ 测试funcition 相关方法 ＝＝"
    run(foo0,1)
    run(foo1,1,2)
    run(foo2,1,2,3)

    run2(foo0, key1="v1", key2="v2")







    """  ====Reference====
    filter(function, sequence)：对sequence中的item依次执行function(item)，将执行结果为True的item组成一个List/String/Tuple（取决于sequence的类型）返回：
    >>> def f(x): return x % 2 != 0 and x % 3 != 0
    >>> filter(f, range(2, 25))
    [5, 7, 11, 13, 17, 19, 23]
    >>> def f(x): return x != 'a'
    >>> filter(f, "abcdef")
    'bcdef'


    map(function, sequence) ：对sequence中的item依次执行function(item)，见执行结果组成一个List返回：
    >>> def cube(x): return x*x*x
    >>> map(cube, range(1, 11))
    [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    >>> def cube(x) : return x + x
    ...
    >>> map(cube , "abcde")
    ['aa', 'bb', 'cc', 'dd', 'ee']
    另外map也支持多个sequence，这就要求function也支持相应数量的参数输入：
    >>> def add(x, y): return x+y
    >>> map(add, range(8), range(8))
    [0, 2, 4, 6, 8, 10, 12, 14]


    reduce(function, sequence, starting_value)：对sequence中的item顺序迭代调用function，如果有starting_value，还可以作为初始值调用，例如可以用来对List求和：
    >>> def add(x,y): return x + y
    >>> reduce(add, range(1, 11))
    55 （注：1+2+3+4+5+6+7+8+9+10）
    >>> reduce(add, range(1, 11), 20)
    75 （注：1+2+3+4+5+6+7+8+9+10+20）


    lambda：这是Python支持一种有趣的语法，它允许你快速定义单行的最小函数，类似与C语言中的宏，这些叫做lambda的函数，是从LISP借用来的，可以用在任何需要函数的地方：
    >>> g = lambda x: x * 2
    >>> g(3)
    6
    >>> (lambda x: x * 2)(3)
    6


    我们也可以把filter map reduce 和lambda结合起来用，函数就可以简单的写成一行。
    例如
    kmpathes = filter(lambda kmpath: kmpath,
    map(lambda kmpath: string.strip(kmpath),
    string.split(l, ':')))
    看起来麻烦，其实就像用语言来描述问题一样，非常优雅。
    对 l 中的所有元素以':'做分割，得出一个列表。对这个列表的每一个元素做字符串strip，形成一个列表。对这个列表的每一个元素做直接返回操作(这个地方可以加上过滤条件限制)，最终获得一个字符串被':'分割的列表，列表中的每一个字符串都做了strip，并可以对特殊字符串过滤。
    """


