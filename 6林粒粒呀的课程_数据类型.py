# 要来高深一点的了：数据类型
'''
字符串 str    'spaces'  "你好"
整数 int(9)   int(-80)
浮点数   float（9.00）
布尔值 bool(True ,False)  T 和F 一定要大写
空值类型 None
#
'''
print(len('hello world'))  # len显示字符串的长度  完整的转义符占位一个长度 \n

print('world hello'[4])  # []内的数字是该字符串的第几个字母。需要注意的是，字符串字母顺序从零开始

# 当你不知道当前变量的类型时，使用type函数，可以返回当前数据的类型

print(type('hello'))  # --->class 'str'

# 不同的数据类型，应用不同的函
s = 'hello world'
print(len(s))
print(type(s))
print(s[8])  # []只能获取一个字符。切记从零开始
print(s[10])
print(s[len(s)-1])

#布尔值
b1=True
b2=False  #不要用小写，也不要用括号，也不用引号（用引号是字符串）

#空值
n=None

#用type函数来验证

print(type(s))
print(type(b1))
print(type(n))

# print(type(s,b1,n))  为啥不能连续type?