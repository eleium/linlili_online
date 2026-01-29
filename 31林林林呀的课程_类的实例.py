#创建一个学生的类，要求：
#1，属性要求包括：姓名，学号，语、数、英三科的成绩
#2,能够设置学生某科目的成绩
#3，能够打印出该学生的所有科目成绩

class Student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        self.grades={'语文':0,'数学':0,'英语':0}#grades:成绩
    def set_grades(self,course,grades):#course:科目
        if course in self.grades:
            self.grades[course]=grades
    def print_grades(self):
        print(f'学生{self.name}的学号是{self.student_id},成绩是：')
        for course in self.grades:
            print(f'{course}:{self.grades[course]}分')

chen=Student('小陈',10086)
wang=Student('小王',10000)
wang.set_grades('数学',88)
print(chen.name,wang.name)
print(wang.grades)
chen.print_grades()
