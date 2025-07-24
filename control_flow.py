# 控制流示例

# if-elif-else 条件判断
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"

print(f"分数: {score}, 等级: {grade}")

# for 循环
fruits = ["apple", "banana", "cherry"]
print("水果列表:")
for fruit in fruits:
    print(f"- {fruit.capitalize()}")

# while 循环
count = 5
print("倒计时:")
while count > 0:
    print(count)
    count -= 1
print("发射!")

# 列表推导式
squares = [x**2 for x in range(1, 6)]
print(f"1-5的平方: {squares}")
