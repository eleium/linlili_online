#不用写重复的代码，可以用类的继承
#子类继承父类的属性和方法，也可以有自己的属性与方法，并且自己的优先.
"""
A属于、是B :class A(B):
人是动物： class Human(Animal):
新能源车是属于车辆： class Electric_car(Car):
"""

#类的继承的练习：人力系统
#员工分为两类：全职员工：FullTimeEmployee、兼职员工：PartTimeEmployee
#全职和兼职员工都有'姓名name'、'工号id'属性
#都具备’打印信息print_info'(打印员工的姓名、工号）方法
# 全职有'月薪monthly_salary'属性
#兼职的有'日薪daily_salary'和'每月上班日数work_days'属性
#全职与兼职都有'计算月薪calculate_monthly_pay'的方法，但是具体计算过程不一样。

class Employee:

    def __init__(self,name,id):
        self.name=name
        self.id=id
    def print_info(self):
        print(f'员工{self.name}的工号是{self.id}')

class FullTimeEmployee(Employee):
    def __init__(self,name,id,monthly_salary):
        #继承父类Employee的name和id 的属性，注意格式：
        super().__init__(name,id)
        self.monthly_salary=monthly_salary

    def calculate_monthly_pay(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self,name,id,daily_salary,work_days):
        #继承父类Employee的name和id的属性，注意格式：有括号，有点
        super().__init__(name,id)
        self.daily_salary=daily_salary
        self.work_days=work_days
    def calculate_monthly_pay(self):
        return self.daily_salary*self.work_days

wang=FullTimeEmployee('小王','10086',1000)
li=PartTimeEmployee('小李','10000',200,30)
wang.print_info()
li.print_info()

#以下两种方法都可以，第二种更明确子类从父类继承来的属性和方法
# print(f'员工{wang.name}的id是{wang.id},月薪是{wang.monthly_salary}')
print(f'员工{wang.name}的id是{wang.id},月薪是{wang.calculate_monthly_pay()}')

# print(f'员工{li.name}的id是{li.id},月工资是{li.daily_salary*li.work_days}')
print(f'员工{li.name}的id是{li.id},月工资是{li.calculate_monthly_pay()}')