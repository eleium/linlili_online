# 列表：

# 列表中的字符串要加引号包裹。

list1 = [12, 4, '中医', 'shoppingmall', 'car']  # 方括号前面不要加list了。
# list1=list([12,4,'中医','shoppingmall','car'])   #除非再加个圆括号。

# append "方法--->增加元素"：
list1.append('苹果')  # 给列表里面添加元素，即列表式可变的。这点不同于字符串、整数、浮点数、布尔值。
# 要变化字符串、整数、浮点数、布尔值，就要重新赋值

print(list1)

# 方法的操作：  对象名.方法()
# 函数的操作：  函数名（）

# remove '方法-->移除元素'
list1.remove(4)
print(list1)
# 可以直接更换元素，用[]代表列表中元素的位置
list1[2] = '西医'
print(list1)

# 一些内置函数：
numbers = [3, 55, -90, 333, 4.444]
print(max(numbers))  # 打印列表中的最大值
print(min(numbers))  # 打印列表中的最小值
print(sorted(numbers))  # 重新排列列表的元素的顺序，从小到大.但是不更改原来的列表numbers。
print(numbers)

# 课程实践：
shopping_list = ['键盘']
# shopping_list.append('音响','硬盘') # 报错，因为append每次只能增加一个元素。
shopping_list.append('音响')
shopping_list.append('硬盘')
shopping_list.append('显示器')
shopping_list.remove('显示器')
print(shopping_list[1])
shopping_list[1] = '内存条'
print(shopping_list)

price = [400, 800, 1000]
print(max(price))
price_max = max(price)
price_min = min(price)

print(price_max, price_min)
print(sorted(price))
