# 异常处理示例

# 基本异常处理
try:
    num = int(input("请输入一个整数: "))
    result = 10 / num
    print(f"10除以{num}的结果是: {result}")
except ValueError:
    print("错误: 请输入一个有效的整数!")
except ZeroDivisionError:
    print("错误: 不能除以零!")
except Exception as e:
    print(f"发生未知错误: {e}")
else:
    print("计算成功!")
finally:
    print("程序执行完毕。")

# 自定义异常
class NegativeNumberError(Exception):
    """负数异常"""
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError("不能使用负数")
    return number

try:
    check_positive(-5)
except NegativeNumberError as e:
    print(f"自定义异常捕获: {e}")
