# 列表list
s = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# 切片操作 (步长为负数，从后向前)
"""print(s[::])
print(s[::-1])
print(s[::-2])
print(s[0::-1])
print(s[1::-2])
print(s[2::-2])
print(s[0::1])
print(s[0:6:-1]) #[]
print(type(s[:6:-1]))
print(s[:-4:1])"""

# 方法
"""list_1 = [1, 2, 3]
list_1.append(4)
print(list_1)
list_1.insert(0,-1)
print(list_1)
list_1.remove(4)
print(list_1)
list_1.pop(0)
print(list_1)
list_1.sort(reverse=True)
print(list_1)

# 删除没有元素不报错
list_1.remove(4)
print(list_1)
list_1.pop(4)
print(list_1)"""

# 将用户输入的10个元素存储到列表中，排序，输出最小值，最大值和平均值
# input_1 = [int(input('输入10个数字:')) for _ in range(10)] 列表推导式
"""while True:
    input_1 = input('输入10个数字:').split()
    if len(input_1) < 10:
        print('输入不够，重新输入')
        continue
    else:
        # summ = 0
        data = list(map(int, input_1))
        data.sort()
        # for i in data:
        #     summ += i
        print('最小值：',data[0])
        print('最大值：',data[-1])
        print('平均值：',sum(data) / len(input_1))
        break"""

# 合并两个列表中的元素，并对合并的结果进行去重处理（去除列表中的重复元素）
num_list1 = [19,23,54,64,875,20,109,232,123,54]
num_list2 = [55,80,72,35,60,123,54,29,91]
"""
for i in range(len(num_list2)):
    if num_list1.count(num_list1[i]) >= 0 :
        num_list1.append(num_list2[i])
num_list1.sort()
print(num_list1)"""
#============================================
"""# 合并列表
# 解包，将列表这一类容器的元素拆成一个一个独立的元素
num_list = [*num_list1,*num_list2]
# 去重
new_list = []
for num in num_list:
    if num not in new_list:
        new_list.append(num)
print(new_list)"""

# 列表推导式 快速按照一定规则生成列表 -> [要插入的值 for i in 序列/列表 [if 条件]]
# 生成1-20平方列表
sqrt_list = [i ** 2 for i in range(1,21)]
print(sqrt_list)
# 提取所有偶数计算平方，组成新的列表
num_list = [12,32,45,77,80,92,33,57,97,98]
new_list = [i ** 2 for i in num_list if i %2 == 0]
print(new_list)










