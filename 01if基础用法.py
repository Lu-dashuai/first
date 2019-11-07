# fag = False
# name = input('请输入姓名：')
# if name == 'python':
#     fag = True
#     print('welcome boss')
# else:
#     print(name)
# age = int(input("请输入你家够的年龄："))
# if age <= 0:
#     print("你是在逗我把")
# elif age == 1:
#     print("相当于14岁的人")
# elif age == 2:
#     print("相当于22岁的人")
# elif age > 2:
#     human = 22 + (age - 2)*5
#     print("相当与人的年龄%d"%human)
# # 退出提示
# input("点击enter键退出")

o = 30
bo = True
while bo:
    num = int(input("猜猜这个数字："))
    if num == o:
        print('恭喜老铁，猜对了')
        bo = False
    elif num > o:
        print('不好意思，猜大了')
    else:
        print('不好意思猜小了')
