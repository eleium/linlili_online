# 把打开的文件赋值给一个变量名：临时的文件名
# 读 read
file_temp = open("d:/python_learning/PythonProject_林粒粒呀课程_电脑上/例子.py", 'r', encoding='utf-8')
print(file_temp)
file_temp.close()

# 写 write (覆盖原文）
file_temp = open("d:/python_learning/PythonProject_林粒粒呀课程_电脑上/例子.py", 'w', encoding='utf-8')
# content:内容的意思。
content = '''风雨凄凄，鸡鸣喈喈。
既见君子，云胡不夷？

风雨潇潇，鸡鸣胶胶。
既见君子，云胡不瘳？

风雨如晦，鸡鸣不已。
既见君子，云胡不喜？。'''
file_temp.write(content)
file_temp.close()

file = open('d:/python_learning/PythonProject_林粒粒呀课程_电脑上/例子.py', 'r', encoding='utf-8')

print(file.read())
file.close()

# 可以把上述文件的路径命名为一个路径名，这样就更方便了：
file_path = 'd:/python_learning/PythonProject_林粒粒呀课程_电脑上/例子.py'
file_temp = open(file_path, 'r', encoding='utf-8')
print(file_temp)
file_temp.close()

# 另外一种读取文件的方法 with ,这种方法不需要再后面用close()方法了。文件自动关闭。
with open(file_path, 'r', encoding='utf-8') as file_temp:
    print(file_temp.read())
#用for循环打印所有行：
with open(file_path,'r',encoding='utf-8') as f:
    lines=f.readlines()
    for line in lines:
        print(line)