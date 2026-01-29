'''
函数定义后，传入的参数计算的结果，只在作用域内起作用。
在函数内定义的变量都是局部变量。
'''
from unicodedata import category
from win32con import BSF_MSGSRV32ISOK_BIT


def function():
    a = 3
    print(a)


# a=3只在函数内部被定义，
# print(a)会提示a没被定义

# 课堂实践
'''
写一个计算BMI的函数，函数名为calculate_BMI.
1,可以计算任意的体重和身高的BMI值。
2，执行的过程中打印一句话：''你的BMI分类为：XX''
3,返回计算出的BMI值。

BMI=体重/(身高**2）

BMI分类：
偏瘦：BMI<=18.5
正常:18.5<=BMI<=25
偏胖：25<=BMI<=30
肥胖：BMI>30
'''


def calculate_BMI(weight, height):
    BMI = weight / (height ** 2)
    if BMI <= 18.5:
        category = '偏瘦'
        print(f'阁下的BMI分类为：偏瘦。')
    elif 18.5 <= BMI <= 25:
        category = '正常'
        print(f'阁下的BMI分类为：正常')
    elif 25 <= BMI <= 30:
        category = '偏胖'
        print(f'阁下的BMI分类为：偏胖')
    else:
        category = "肥胖"
        print(f'阁下的BMI分类为：肥胖')

    # print(f'{BMI:.2f}')
    return BMI#函数执行到此就结束了。不会再执行后面的代码（在正常缩进内的，是def的语句。）


# calculate_BMI(80, 1.73)  如果要打印本参数的结果，这行就不需要了。
current_BMI = calculate_BMI(80, 1.73)
print(f'阁下当前的BMI值为：{current_BMI:.3f}')
