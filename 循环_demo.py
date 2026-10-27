# while
# 计算1-100之间所有偶数的累加之和
"""res = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        res += i
    i += 1

print(res)
print(type(res))"""

# for
# 计算1-100之间所有的奇数之和
"""total_1 = 0
total_2 = 0
for i in range(100):
    if i % 2 == 1:
        total_1 += i

# 计算100-500之间所有的3的倍数的数字之和
for i in range(100,500):
    if i % 3 == 0:
        total_2 += i

print(f"1-100之间所有的奇数之和: {total_1}")
print(f"100-500之间所有的3的倍数的数字之和: {total_2}")"""

# 嵌套循环
# 打印一个倒三角形
"""n = 1 #控制行
count = 0 #控制一行多少颗星
star = '*'
for i in range(n,10):
    print(' ' * (n - 1),end="")
    for j in range(count,10):
        print(star,end="")
    print("\n")
    n += 1
    count += 2
    if count > 10:
        break"""

# 打印一个心形
"""for y in [1.5 - i*0.1 for i in range(30)]:
    line = ""
    for x in [j*0.05 for j in range(-30,30)]:
        # 心形公式判断
        if (x**2 + y**2 - 1)**3 - x**2 * y**3 <= 0:
            line += "*"
        else:
            line += " "
    print(line)"""

# 进阶
"""import math

def heart_r(theta):
    return (2 - 2 * math.sin(theta)
            + math.sin(theta) * math.sqrt(abs(math.cos(theta)))
            / (math.sin(theta) + 1.4))

def draw_heart(width=61, height=31, aspect=2.0):
    r_max = max(heart_r(2 * math.pi * i / 6000) for i in range(6000))
    cx, cy = (width - 1) / 2, (height - 1) / 2
    scale = min(cx, cy) / r_max * 0.95          # 自动缩放铺满画布

    for row in range(height):
        line = ''
        for col in range(width):
            x = (col - cx) / aspect           # 字符坐标 -> 数学坐标 (-30,0) -> (-15,0) 一格-> 1 2格->1
            y = cy - row                        # y 轴翻转
            inside = math.hypot(x, y) / scale <= heart_r(math.atan2(y, x))
            line += '*' if inside else '.'
        print(line)

draw_heart()"""

import math


def heart_r(theta):
    return (2 - 2 * math.sin(theta)
            + math.sin(theta) * math.sqrt(abs(math.cos(theta))) / (math.sin(theta) + 1.4))


def draw_heart(width=61, height=31, aspect=2.0):
    r_max = max(heart_r(2 * math.pi * i / 2000) for i in range(2000))
    cx, cy = (width - 1) / 2, (height - 1) / 2
    scale = min(cx, cy) / r_max * 0.95
    for row in range(height):
        line = ''
        for col in range(width):
            x = (col - cx) / aspect
            y = cy - row
            inside = math.hypot(x, y) / scale <= heart_r(math.atan2(y, x))
            line += '*' if inside else '.'
        print(line)


draw_heart()

# 二次函数 y = ax^2 + bx + c
"""def fun(x):
    return x ** 2 + 2 * x + 1

def draw_fun(width=51, height=101, aspect=2.0):
    cx, cy = (width - 1) / 2, (height - 1) / 2
    for row in range(height):
        line = ''
        for col in range(width):
            x = (col - cx)/aspect
            y = cy - row
            line += '*' if y==fun(x) else '.'
            # if x == 1 and y == 4:
            #     print('找到点')
        print(line)
draw_fun()"""

# 乘法表
"""row = 10
for i in range(1,row):
    line = ''
    for j in range(1,i+1):
        line += f"{j}*{i}={j*i} "
    print(line.rstrip())"""

# break continue
# 用户名密码输入案例
"""while 1:
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if username == '' or password == '':
        print('用户名和密码不能为空！')
        continue
    elif username == 'admin' and password == '666888':
        print('登录成功')
        break
    else:
        print('用户名或密码错误，登录失败')"""

# 猜数字
"""import random

result = random.randint(1, 100)
while True:
    guess = int(input('请输入要猜测的数字：'))
    if guess == result:
        print('猜对了')
        break
    elif guess > result:
        print('猜大了')
        continue
    elif guess < result:
        print('猜小了')
        continue"""
