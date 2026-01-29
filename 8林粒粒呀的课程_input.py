# input函数
input('请输入：你好')  # 单独用input函数，程序会一直等待你输入的内容。
s = input('666')  # input返回的是字符串。 666是显示的内容（提示符），你要输入你希望的内容，而且出来的是str
print(s)
age = input('你今年多大啦？')  # 程序会显示：你今年多大啦？并等待你输入你的年龄
print('知道了' + age + '岁了')

print(int(age) + int(s))
