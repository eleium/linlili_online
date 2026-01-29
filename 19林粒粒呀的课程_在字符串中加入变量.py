# 三种方法在字符串中加入变量： 1，format方法，2，旧的%的方法，3，最方便的 f 方法:f-string格式化字符串。

contacts = ['小李', '小王', '小赵', '小钱', '小张']
year = '虎'

for name in contacts:
    # f-string ,里面的变量用{}包裹。f-string（前面加 f'...'，然后用 {year} 插入变量）

    # f-string 是在字符串前面加上字母 f 或 F，然后用大括号 {} 将表达式括起来，表达式会被求值并格式化成字符串。
    message_content = f'''      
律回春渐，新元肇启，
新岁甫至，福气东来。
金{year}敲门，五福临门。
给{name}及家人拜年啦！
新春快乐，{year}年大吉！
'''
    # 金+{year}+贺岁，欢乐祥瑞，# 在f-string里，不要再用+号，否则+号会被打印出来
    # 金+{year}+敲门，五福临门。
    # 给+{contacts}+及家人拜年啦！
    # 新春快乐，+{year}+年大吉！
    print(message_content)

'''
f-string的详细用法：
1，直接插入变量或表达式
name='bob'
print(f'name:{name}')
2,插入表达式：
number=(a+b)
print(f'the number is {number}')
3,后面接：. f可以定下浮点数的小数点位数：
pi=3.1415926535897932384626
print(f'pi={pi:.3f}')   #用冒号加.nf 来确定输出的小数点位数。
4,使用三引号可以创建多行f-string
age=99
names='adm'
info=f'''
age: {age}
name: {names}
'''
print(info)

'''
