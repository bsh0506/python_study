#转义符
msg = "你好 \n 小明 \"您好\""
print(msg)
print(type(msg))

msg1 = ('姓名\t年龄\t性别\n小明\t23\t男')
print(msg1)
print(type(msg1))

#字符窜拼接
str1 = 'Zeus'
str2 = '23岁'
str3 = '软件工程'
str4 = '男'
print('大家好，我是 '+ str1 + ', 性别 ' + str4 + ', 今年 '+str2 + ', 专业是 ' + str3)

#占位符
print("大家好，我是 %s，性别 %s，今年 %s, 专业是 %s" % (str1, str4, str2, str3))
print(f"大家好，我是 {str1}，性别 {str4}，今年 {str2}, 专业是 {str3}")

print('='* 60)
# 字符串方法案例
# 邮箱格式验证 包含一个@ 包含一个.
"""
input_1 = input('请输入邮箱：')
if input_1.find('@') != -1 and input_1.find('.') != -1:
    print('邮箱格式正确')
else:
    print('邮箱格式错误')"""

# 输入一个字符串，判断字符串是否回文
"""input_2 = input('请输入字符串是否回文：')
str_list1 = list(input_2)
str_list2 = [*str_list1]
str_list2.reverse()
print(str_list1)
if str_list1 == str_list2:
    print('是回文字符串')
else:
    print('不是回文字符串')"""

input_2 = input('请输入字符串是否回文：')
str_new = input_2[::-1]
if str_new == input_2:
    print('是回文字符串')
else:
    print('不是回文字符串')

