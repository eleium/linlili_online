# BMI=体重/（身高**2）

weight = input('你的体重是多少公斤？')  # 记住：现在输出的是字符串，不能计算
height = input('你的身高是多少米？')

# BMI=int(weight)/(int(height)**2)#不能用int函数，否则都是整数：身高1米。
BMI = float(weight) / (float(height) ** 2)  # 用float函数，才能输入真实的身高。

print('您的BMI值为' + str(BMI))
