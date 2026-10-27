# 函数


def add(a, b):
    """
    :param a: 要相加的数
    :param b:
    :return: a,b的和
    """
    return a + b


help(add)
print(add(1, 2))

# 函数说明文档
## 函数名下面用""" """ 引起来的内容 方便调用者使用
## 有多个返回值时返回的类型是元组
"""def circle_area_len(r):
    return round(math.pi * (r ** 2), 2), round(2 * math.pi * r, 1)


area, length = circle_area_len(5)  # 解包
print(circle_area_len(5))

print("=" * 30)"""

# 函数嵌套
"""def function_a():
    print("function_a before")
    function_b()
    print("function_a after")


def function_b():
    print("function_b before")
    function_c()
    print("function_b after")


def function_c():
    print("function_c")


function_a()"""

# 案例
# 定义一个函数：根据传入的底和高计算三角形面积的函数（三角形 = 底 * 高 / 2）
"""def triangle_area(d, g):
    return round(d * g / 2, 2)


# 计算传入字符串中元音字母的个数(aeiouAEIOU)
def count_vowels(s):
    count = 0
    for char in s:
        if char in "aeiouAEIOU":
            count += 1
    return count


# 计算传入班级学员高考成绩列表中成绩的最高分、最低分、平均分（保留一位小数），并返回
def get_score_stats(score_list):
    max_score = max(score_list)
    min_score = min(score_list)
    avg_score = round(sum(score_list) / len(score_list), 1)
    return max_score, min_score, avg_score


print(triangle_area(1, 2))
print(count_vowels("hello"))
print(get_score_stats([15, 16, 30, 60, 80, 50, 90, 40]))"""

# 函数传参方式
"""def reg_stu(name, age, gender, city):
    print(f"姓名：{name},年龄：{age},性别：{gender},城市：{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}"""

# 传参方式一：位置传参
"""res_1 = reg_stu("张三", 18, "男", "大连")
print(f"res_1:{res_1}")"""
# 传参方式二：关键字
"""res_2 = reg_stu(name="张三", city="大连", age=18, gender="男")
print(f"res_2:{res_2}")"""

# 传参方式三：关键字+位置参数 位置参数在前，关键字参数在后

"""def calc_data(*args, **kwargs):
    data = args
    k_v = kwargs
    for k, v in k_v.items():
        print(f"{k}:{v}")
    print(data)


calc_data(1, 2, 3, 4, round=10, pi=3.14)

dict_1 = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6}
print(dict_1)
dict_1.get(1)
print(dict_1[1])"""

# 参数类型
## 特殊参数 ： 函数
"""def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def calc(a, b, oper):
    return oper(a, b)


print(calc(1, 2, oper=add))
print(calc(1, 2, oper=subtract))"""

# 匿名函数
## 完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序
# if a key function is given, apply it once to each list item and sort them, ascending or descending, according to their function values
"""data_list = ["C++", "C", "Python", "Java", "Go"]
print(data_list)
data_list.sort(key=lambda item: len(item))
print(data_list)"""


# ========案例==========
##定义一个函数，根据传入的数字，计算该数字阶乘的结果
def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)


## __name__内置变量 该模块不是直接运行时，__name__ == function_demo ,别的模块import了这个模块，那么这个模块所有的语句都会执行
## 这一句的意思是只有当前模块直接运行才会执行的语句，别的模块执行时不会执行这条语句
if __name__ == "__main__":
    print(factorial(5))
