# 程序异常的类型：
# list index out of range:  索引错误，超出了索引的范围IndexError
list = [23, 44, 656, -43, 534.3]
# list[5]

# 除 0 错误：ZeroDivisionError
# print(88 / 0)

# 找不到文件错误：FileNotFoundError
# open(. / linliliya.py, 'r', encoding = "utf-8")

# 两个字符串做乘法： TypeError
# print('abc' * 'str')

# 语法错误：SyntaxError   缩进错误：IndentationError  属性错误：AttributeError 等等等等........

# 捕捉异常：用try/except语句
try:
    name = input('please input your name.')
    age = int(input('please input your age.'))
    weight = float(input('输入体重'))
    height = float(input('请输入身高'))
    BMI = weight / height

except ValueError:
    print('你输入的值不合理，核对后重新输入。')
except ZeroDivisionError:
    print('零不能当除数')

# 如何你知道会有什么类型的报错，直接用：
except:
    print('你输入的东西类型不对，重新输入')

# try/except语句从上往下执行，有一个符合的就不会再往下执行
else:
    print(f'你的BMI值是：{BMI:.3f}')

# finally语句：不管except有没有捕捉到错误，或者程序炸了，finally语句都会被执行：飞翔吧，程序！
finally:
    print('飞翔吧，程序！')
