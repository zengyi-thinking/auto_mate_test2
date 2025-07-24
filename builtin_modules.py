# 常用内置模块示例

import os
import sys
import json
import pathlib

# os模块 - 操作系统交互
print(f"当前工作目录: {os.getcwd()}")
print(f"系统环境变量: {os.environ.get('PATH')}")

# sys模块 - 系统参数
print(f"Python版本: {sys.version}")
print(f"命令行参数: {sys.argv}")

# json模块 - JSON处理
data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "hiking", "coding"],
    "is_student": False
}

# 转换为JSON字符串
json_str = json.dumps(data, indent=2)
print("JSON字符串:")
print(json_str)

# 从JSON字符串加载
loaded_data = json.loads(json_str)
print(f"从JSON加载的数据: {loaded_data['name']}")

# pathlib模块 - 路径操作
current_dir = pathlib.Path.cwd()
print(f"当前目录: {current_dir}")
new_file = current_dir / "new_file.txt"
new_file.touch()
print(f"创建新文件: {new_file}")
