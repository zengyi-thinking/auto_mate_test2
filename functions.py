# 函数示例

# 基本函数
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# 带默认参数的函数
def power(base, exponent=2):
    return base ** exponent

print(f"5的平方: {power(5)}")
print(f"2的3次方: {power(2, 3)}")

# 可变参数
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"求和: {sum_all(1, 2, 3, 4, 5)}")

# lambda 函数
double = lambda x: x * 2
print(f"10的双倍: {double(10)}")
