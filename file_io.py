# 文件操作示例

# 写入文件
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("这是第一行文本\n")
    file.write("这是第二行文本\n")
    file.write("Python文件操作很简单!\n")

print("文件写入完成")

# 读取文件
print("\n文件内容:")
with open("example.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())  # 去除行尾换行符

# 追加内容
with open("example.txt", "a", encoding="utf-8") as file:
    file.write("这是追加的内容\n")

print("\n追加后的内容:")
with open("example.txt", "r", encoding="utf-8") as file:
    print(file.read())
