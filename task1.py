# 创建一个类 包含 get_name 和 age
class User:
    # 添加公共的信息
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear
    def get_name(self):
        # 占位符
        # pass
        return self.name

    def age(self, current_year):
        # 计算年龄
        age = current_year - self.birthyear
        return age

user = User('PPX', 1990)
print(user.age(2024)) # 34
print(user.get_name()) # PPX