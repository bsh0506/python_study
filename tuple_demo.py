# -------元组 解包，组包-----------
# 组包操作

t1 = (1, 2, 3, 5, 6)
t2 = 1, 2, 3, 4, 5, 6
# 解包
a, b, c, d, e = t1
first, *middle, last = t1

print(t1)
print(t1[0])
print(t2)
print(first)
print(middle)
print(type(middle))
print(last)

middle = list(middle)
print(middle)
