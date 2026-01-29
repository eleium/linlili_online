# 创建一个叫猫的类
class Cat:
    # 通过__init__方法构造这个叫Cat的类的属性有：名字，年龄，颜色
    def __init__(self, cat_name, cat_age, cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color


# 通过Cat(属性）来具体调用这个叫cat_1的类的属性并赋值
cat_1 = Cat('糖宝', 2, 'yellow')
# cat_1.name,cat_1.age,cat_1.color就是cat_1这个实例的属性
print(f'我的猫叫{cat_1.name},{cat_1.age}岁大了，它是{cat_1.color}色的。')
