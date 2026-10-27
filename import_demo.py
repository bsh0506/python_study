# 模块 导入

import os

# 从别的模块导入
import function_demo

print(os.getcwd())
print("=" * 30)
print(os.path.abspath("."))
print("=" * 30)

# function_demo 的 factorial函数
print(function_demo.factorial(5))
print("=" * 30)
