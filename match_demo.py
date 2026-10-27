# 基于match_case 实现一个简易计算器，可以实现 + - * / 运算，用户输入需要运算的两个数和运算符之后，就可以进行计算
data = input('请输入要计算的两个数：').split()
ysf = input('请输入要运算的运算符：')
data_map = map(int,data)
data_list = list(data_map)
a = data_list[0]
b = data_list[1]
match ysf:
    case "+":
        res = a + b
    case "-":
        res = a - b
    case "*":
        res = a * b
    case "/":
        res = a / b
    case _:
        res = 0

print(f'运算结果为{res}')

