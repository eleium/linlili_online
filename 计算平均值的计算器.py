
#用户可以输入任意数量的数字，最后输入q，表示数字输入完成，然后程序给出平均值计算的结果。

user_input=input('请输入数字,完成输入后，请输入q以终止输入程序')

total=0
count=0
while user_input != "q":
    user_input=input('请输入数字，完成后以q来终止输入')