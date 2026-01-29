# 变量
'''
1，不能有空格
2，不能用数字打头
3，不能用引号包裹
'''

my_love_number = 18666666666  # 这叫赋值操作。给变量名赋值。
print('拨打' + 'my_love_number')  # 这是两个字符串连接： 拨打my_love_number

# print('拨打'+my_love_number)
# 这个是错误。因为'拨打'是字符串，my_love_number是数字。要加str: 如下：
print('拨打' + str(my_love_number))

my_ex = my_love_number  # 可以给变量赋值，此时my_ex的值就是18666666666.
my_love_number = 13066666666  # 给原来的变量赋值新值，而原my_ex的值不变。
print(my_ex)  # 18666666666
print(my_love_number)  # 13066666666

greet = "你好，吃了吗"
print(greet + ' 张三?')
print(greet + ' 李四?')
print(greet + ' 王五?')
greet_chinese=greet
greet_english='hi!mybaby'
greet=greet_english

# greet = "hi!baby!"  # 变量的值可以随时更换
print(greet + ' 张三?')
print(greet + ' 李四?')
print(greet + ' 王五?')


print(greet_english+'老王')
print(greet_chinese+'老李')

