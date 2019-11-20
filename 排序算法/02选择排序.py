# coding:utf-8
"""
选择排序
    内层循环：通过第一个（min=0,假定第一个就是最小的，坐标为0）元素 和其他所有元素进行比对，每次的比对记录较小值的下标，比较完将通过记录的下标所在的值 替换 第一个值
    外层循环：控制循环次数，决定从第一个（j）开始，替换内层循环的min
            总共7个数据，可以执行6遍，最后一个后面没了，所以比较到最后一个的前面一位，所以循环遍数为len-1，
"""


def select_sort(alist):
    print("排序后：", alist)


if __name__ == "__main__":
    print("进入主方法")
    alist = [1, -2, -3, 400, 9, 0, -100]
    print("排序前：", alist)
    for j in range(len(alist) - 1):
        min = j
        for i in range(j + 1, len(alist)):
            if alist[min] > alist[i]:
                min = i
        alist[j], alist[min] = alist[min], alist[j]
    print("排序后：", alist)
