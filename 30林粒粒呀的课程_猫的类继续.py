# 创建一个叫猫的类
class Cat:
    # 通过__init__方法构造这个叫Cat的类的属性有：名字，年龄，颜色
    def __init__(self, cat_name, cat_age, cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color

    # 以上的例子定义了一个猫的属性。还可以定义猫的方法：即对象能干啥事:
    # 与普通定义函数一样，但是要缩进在class类下面，表示是该类的方法：
    def speak(self):  # 括号内必须写self.
        # 与__init__一样，第一个参数被占用，用self命名，表示实例。
        print('喵' * self.age)


# 通过Cat(属性）来具体调用这个叫cat_1的类的属性并赋值
cat_1 = Cat('糖宝', 5, 'yellow')
# cat_1.name,cat_1.age,cat_1.color就是cat_1这个实例的属性
print(f'我的猫叫{cat_1.name},{cat_1.age}岁大了，它是{cat_1.color}色的。')

# 要调用方法：对象.方法名()，括号内不需要写self，自动调用对象的方法
cat_1.speak()
