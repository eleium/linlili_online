# 用代码代替计算器
# 在pycharm中，数字 不要用引号包裹，不然会被认作字符串。而字符串与数字是不能连接和计算的。
# 带小数点的是浮点数，不带的是整数。

print(1 + 2 - 3 * 4 / 5)

print((2 ** 3))  # 2的3次方的写法 两个**是乘方的意思，后面的数字是几次方。

# 导入数学函数库
import math

# math.(函数名) 此时可以使用数学函数的功能了
math.log(2, 3)
bb = math.sin(45)
cc = math.cos(90)
aa = math.log(2, 3)
print(aa, bb, cc)
# print((aa,\nbb,\ncc))

print(math.log2(3))

# 举例子：

# -x**2-2x+3=0
# x**2+2x-3=0
#  ax**2+bx+c=0
a = 1
b = 2
c = -3
x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
print(x1, x2)
# 以上的代码中，每个乘除、平方等等都要加上乘号 * ，不然报错。 4a是错的， 4*a是对的。
'''1，可以看到整个公式，随时检查。
2，方便的更替变量的值。
3，如果公式复杂，可以给公式中的固定项命名，更快捷： sqrt_1=(b**2-4*a*c)'''
sqrt_1 = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(sqrt_1)) / (2 * a)
x2 = (-b - math.sqrt(sqrt_1)) / (2 * a)
print(x1, x2)
# 别忘了开始要import math

# shit ,怎么也没办法把这个文件推到github的仓库中
# 也不是很难。已经搞定了如何推送到github的指定仓库中。原来就是在推送界面选择origin:master
