# 模块和包示例

# 导入整个模块
import math

print(f"圆周率: {math.pi}")
print(f"16的平方根: {math.sqrt(16)}")

# 导入特定函数
from datetime import datetime, timedelta

now = datetime.now()
print(f"当前时间: {now}")
tomorrow = now + timedelta(days=1)
print(f"明天此时: {tomorrow}")

# 别名导入
import random as rd

random_number = rd.randint(1, 100)
print(f"随机数 (1-100): {random_number}")

# 创建自己的模块
# 创建一个名为 mymodule.py 的文件，包含以下内容:
"""
# mymodule.py
def say_hello(name):
    return f"Hello, {name} from mymodule!"

version = "1.0"
"""
# 然后在当前文件中导入:
# import mymodule
# print(mymodule.say_hello("Alice"))
