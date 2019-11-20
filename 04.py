# coding:utf-8
from timeit import Timer


def t1():
    li = []
    for i in range(1000):
        li.append(i)


def t2():
    li = []
    for i in range(1000):
        li += [i]


def t3():
    li = (i for i in range(1000))


def t4():
    li = list(range(1000))


timer1 = Timer("t1()", "from __main__ import t1")
print(timer1.timeit(1000))
