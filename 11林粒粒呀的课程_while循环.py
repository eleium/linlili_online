# 另外一个循环方法：while:

# 如果用 for i in range(100): ,也就循环100次，没有时间概念,天没黑就循环完了。。
# measure_brightness函数返回当前测量的天空亮度

measure_brightness = int(input('当前的天空亮度'))
# if measure_brightness >= 500:
# 执行拍摄
# take_photo()
# 用if语句来判断，只能判断一个条件，只能执行一次拍摄操作。

# while 语句只判断条件的True或False,如果条件A一直为真，就一直执行B，直到条件A为假，退出循环。
# while 条件A：如果为真，就一直执行B。如果条件A为假，就退出循环。
#     执行B

# while measure_brightness>=500:
# take_photo()        带括号表示是个函数，可以执行。

# 打印出列表中的每个元素
list1 = ['你', '好', '吗', '兄', '弟']

for char in list1:
    print(char)

for i in range(len(list1)):
    print(list1[i])

i = 0
while i < len(list1):  # len(list1)代表列表中的元素的长度
    print(list1[i])  # 打印列表中的第i个元素
    i = i + 1  # 为啥这个要写在print的后面？放在前面就从i=i+1，也就是1开始。而列表的序列从0--到n-1。
    #
# for循环在有明确的循环对象和循环次数的时候更方便
# while循环更通用，特别是不知道要循环多少次的时候

# 课程实践：利用while循环，写一个对用户输入数字求平均值的计算器。
# 用户可以输入任意数量的数字，最后输入q，表示数字输入完成，然后程序给出平均值计算的结果。

user_input = input('请输入数字,完成输入后，请输入q以终止输入程序')

total = 0  # 数字的和
count = 0  # 数字的个数

while user_input != "q":
    num=float(user_input)
    # total=total+num
    total+=num
    # count=count+1
    count+=1
    user_input = input('请输入数字，完成后以q来终止输入')
if count==0:
    result=0
else:
    result=total/count
print('你输入的数字平均值为'+str(result))
