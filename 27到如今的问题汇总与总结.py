'''
1,数学计算符号的确切含义，用法：%求模，//地板整除法， **幂，求方，求根号？
2，for 循环 ，遍历的格式
3，if 判断，elif ,else
4,while 循环的格式，与for循环的不同在哪
5，def 函数的结构，每一个代码的含义，return返回到哪里，如何调用函数。
6，字符串可以与int(float)互换，字符串的元素操作方法：append,remove,add,sorted
7,字符串的string-len，元素计算，元素的位置
8，元组tuple，字符串str，整数int，浮点数float，列表list[]，字典dictionary,{key,value},集合set{}的可变性
9，转义符\n，多行
10，input输入
11，字符串的格式化： f'  " 与string.format，忽略的%用法。
12,导入模块的方法：1 import math 2,form math import statistics  3,form math import *
13,模块：一个函数构成，代表一个功能，包括一个函数，变量，类，甚至是其他模块。
   库：多个模块构成，一个安装包，一个功能的集合，包括多个模块，文件夹__init__.py，
   类class：面向对象的结构，包括对象的属性，功能，行为等。属性是数据，方法是函数
14，函数、类的定义有没有严格的格式？

'''
#函数的定义格式：
# def function_name(parameter1,参数2,......):
    #缩进4个空格
    #函数体（代码块）

def sum_1(a,b):
    return a+b
a=5
b=8
result=sum_1(a,b)
print(result)