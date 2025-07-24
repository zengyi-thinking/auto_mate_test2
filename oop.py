# 面向对象编程示例

# 基本类
class Dog:
    # 类属性
    species = "Canis familiaris"
    
    # 初始化方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # 实例方法
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"

# 创建实例
my_dog = Dog("Buddy", 3)
print(my_dog.description())
print(my_dog.speak("Woof Woof!"))

# 继承
class GoldenRetriever(Dog):
    def speak(self, sound="Bark!"):
        return super().speak(sound)

    def fetch(self):
        return f"{self.name} is fetching"

goldie = GoldenRetriever("Goldie", 2)
print(goldie.speak())
print(goldie.fetch())
