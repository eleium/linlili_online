# for 变量名 in 可迭代的对象:

# 作用就是对 每一个变量做一些事情
temperature_list = [35, 56, 38.2, 28]
for temperature in temperature_list:  # 遍历temperature_list 中的每一个列表变量，然后。。。
    # 这时候 temperature可以随便，如temp, hi ,等，会被依次赋值为列表中的每一个变量值：35,56,38.2
    # for语 句下面，所有带缩进的语句，都视为for循环的内容，对每个元素都执行一遍
    if temperature > 38:
        print('The man is dead.')
        print('完球了！')
# 有多少个 >38的，就打印多少次‘完球了’。即遍历所有元素，条件符合就执行一次。

for temp in temperature_list:
    if temp < 38:  # temp 与上面的temperature 没啥不同，都是临时变量，可以任意：temp, x,item等等
        print('太冷血了。')

second_temp = {'小王': 36.5, '小李': 37, '小张': 38.5, '小赵': 42, '小钱': 38}
# for temp in second_temp:#在循环体里的 temp 是 "小王", "小李", "小张"键名，字符串类型，而不是温度。
for temp in second_temp.values():  # 一定要加上()
    # second_temp.values是 方法。代表着集合中的值。
    # 相应的是 second_temp.keys,代表集合中的键。  两者都要用复数 s.
    # 要使用方法，就要在方法的后面加上()，表示 使用该方法
    if temp > 38:
        print('热死额')
    # if temp<38:#这里应该用elif
    elif temp < 38:  # elif 后面要加上条件，else后面不需要，直接用冒号：
        print('冷啊')
        # print('冷死了')
    else:
        print('刚刚好，真舒服')

# if: 如果。
# elif :否则或者，上面的if不为真时，还可以用这个（这些）判断条件。 是else if 的简写。要加判断语句。
# else:否则。以上所有的if ,和elif 都不为真的时候，就执行这个。不需要判断语句，直接冒号。

# 还可以用item()，同时取 键值对。
for staff, temp in second_temp.items():
    if temp > 38:
        print(staff, '烧死啦')
    elif temp < 38:
        print(staff, '冻死人了')
    else:
        print(staff, '今天很舒服啊')

# range的用法： 整数数列
# range(5,10) 数列从5遍历到10但不包括10，即：5,6,7,8，，9。括号内第一个是起始值，后一个是结束值，但不包含。
# range(1,10,2):从1到9的以2为步长的数列：1,3,5,7,9:  2 就是步长。
for i in range(1, 10):
    print(i)

total = 0
for i in range(1, 101):
    total = total + i
    # 如果是total=total+1,每次循环给total加1，所以总和是循环次数：100。
    # 是每次加 1，最终 total 的值是累加了100次的1，即100。

    # total+i,是每次从数列里取一个值，再加上上次的值。
    # 是将当前循环的 i 值 累加到 total 中，也就是累加所有的序列值。即：1+2+3+...+100.
    print(total)
