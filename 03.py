# 如果a+b+c=1000,a^2+b^2=c^2,求abc可能的组合？
import time

# 方法1：
# start_time = time.time()
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
#                 print("a,b,c:%d,%d,%d" % (a, b, c))
# end_time = time.time()
# print("共用时：%d" % (end_time - start_time))

# 方法二：
start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000-a-b
        if a ** 2 + b ** 2 == c ** 2:
            print("a,b,c:%d,%d,%d" % (a, b, c))
end_time = time.time()
print("共用时：%d s" % (end_time - start_time))