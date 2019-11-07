#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
list1 = []

for i in range(1, 5):
    for j in range(1, 5):
        for z in range(1, 5):
            if i != j != z:
                print(str(i) + str(j) + str(z))
                str1 = str(i) + str(j) + str(z)
                list1.append(str1)
print(list1)
print(len(list1))

# 知识点：range(1,5) 表示 [1,5) 的数据集合
