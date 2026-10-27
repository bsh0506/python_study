"""# 判断用户输入的数字是奇数还是偶数
input_1 = int(input('请输入数字：'))
if input_1 % 2 == 1:
    print('input_1是奇数')
else :
    print('input_1是偶数')

# 判断用户是否已经成年
input_2 = int(input('请输入年龄：'))
if input_2 > 18:
    print('成年')
else:
    print('未成年')

# 判断该数字是正数还是负数（不考虑0）
input_3 = int(input('请输入数字：'))
if input_3 > 0:
    print('input_3是正数')
elif input_3 < 0:
    print('input_3是负数')
else:
    print('输入无效')

# 判断用户输入的分数是否及格（大于等于60就是及格）
input_4 = int(input("请输入分数："))
if input_4 >= 60:
    print('及格了')
else:
    print('不及格')"""

"""# 用户输入用户名和密码判断登录是否成功
username = input('请输入用户名：')
password = input('请输入密码：')
if username == 'admin' and password == '666888':
    print('登录成功')
elif username == 'root' and password == '547527':
    print('登录成功')
elif username == 'zhangSan' and password == '123456':
    print('登录成功')
else:
    print('登录失败')"""


# 输入三角形三边长，判断三角形类型
data = input('请输入三角形三边长:').split()
data_sel = map(int, data)  #data_sel为map类实例
data = list(data_sel)
data_res = data.sort()
a = data[0]
b = data[1]
c = data[2]
if a + b <= c:
    print('不是三角形')
elif a == b or b == c:
    if a == c:
        print('是等边三角形')
    else:
        print('是等腰三角形')
else:
    print('是普通三角形')

