# 文件路径过长，但是在引号内，可以直接换行。路径必须用引号括起来。
# 原文件python_file_opration.txe不是 utf-8编码，所以会报错。可以在open（）内不写encoding='utf-8'.
f = open(
    'D:/python_learning/PythonProject_林粒粒呀课程_电脑上/python_file_opration.txt',
    "r", encoding='utf-8'
)
print(f.readline())
# 如果读两遍，第二遍会是空文件，因为上一个已经读到了末尾
# print(f.read())

f.close()

# 如果文件非常大，不要用read一次读完，会爆内存。给他个限制： read(100),只读1-100字节里的内容。
# 下次：read(100),读101-200字节的内容
# 读文件的三种方法： read:返回所有内容的字符串
# readline：读第一行，返回这一行的字符串。与while 联合，只要返回的不是空字符串，就一直读。
# readlines：逐行读，返回所有行的字符串的一个列表
f1 = open(
    'D:/python_learning/PythonProject_林粒粒呀课程_电脑上/python_file_opration.txt',
    'w', encoding='utf-8'
)
content = '我喜欢唐诗'
f1.write(content)
f1.close()

f1 = open(
    'D:/python_learning/PythonProject_林粒粒呀课程_电脑上/python_file_opration.txt',
    "r", encoding='utf-8'
)
print(f1.readline())

###完蛋，把原来的内容覆盖了，只剩下：我喜欢唐诗~~~~~~~
