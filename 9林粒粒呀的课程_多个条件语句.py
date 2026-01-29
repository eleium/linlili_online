# 如果有多个条件语句，并列的而非嵌套的，那么python会一直找到条件为真的，再进行执行语句。即： 或者
#
# if [条件1]：如果为True ,就执行1。如果为False，就进入elif的条件2判断
#     执行1
# elif [条件2]:如果为True,就执行2。如果为False，就判断条件3。
#     执行2
# elif [条件3]:
#     执行3
# else:     如果上面所有的都为False,就执行4.
#    执行4

# 如果条件1为假，条件2和3都是真的，python 只会执行到条件2就结束了，不会再执行挑拣。

# 课程实践

# BMI=体重/（身高**2）

weight = input('你的体重是多少公斤？')  # 记住：现在输出的是字符串，不能计算
height = input('你的身高是多少米？')

# BMI=int(weight)/(int(height)**2)#不能用int函数，否则都是整数：身高1米。
BMI = float(weight) / (float(height) ** 2)  # 用float函数，才能输入真实的身高。

print('您的BMI值为' + str(BMI))
# 偏瘦:BMI<=18.5
# 正常:18.5<BMI<=25
# 偏胖：25<BMI<=30
# 肥胖：BMI>30

if BMI <= 18.5:
    print('你要多吃点，现在偏瘦。')
elif 18.5 < BMI <= 25:
    print('你的身材正常。')
elif 25 < BMI <= 30:
    print('有点偏胖哦。')
else:
    print('赶紧减肥，你肥胖啦')
