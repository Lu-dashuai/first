# coding:utf-8
"""
冒泡排序：
比如这个数据有10个，长度是10，最后一位数的坐标为9
那么 双层循环嵌套：
                j 外层循环表示进行几次从前到后的两两对比
                i 内层循环表示每次从头开始两两对比的次数
随着从头开始比较次数的增多，内层需要凉凉对比的次数减少。
    len = 10
 j   i
 1   9
 2   8
 3   7
 4   6
 ...

 j = len - 1
 i = len - 1 - j



"""
def maopao_sort(alist):
    for j in range(len(alist) - 1):
        for i in range(len(alist) - j - 1):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
    print("排序后：", alist)


if __name__ == "__main__":
    print("进入主方法")
    alist = [1, -2, 3, 400, 9, 0, 100]
    print("排序前：", alist)
    maopao_sort(alist)
