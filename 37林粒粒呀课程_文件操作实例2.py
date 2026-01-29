# 任务1：在一个新的名字为"poem.txt"的文件里，写入一下内容：
# 我欲乘风归去，
# 又恐琼楼玉宇，
# 高出不胜寒。

# 任务2：在上面的"poem.txt"文件结尾处，添加以下两句：
# 起舞弄清影，
# 何似在人间。

with open('d:/python_learning/PythonProject_林粒粒呀课程_电脑上/poem.txt', 'w', encoding='utf-8') as f:
    content = '''
我欲乘风归去，
又恐琼楼玉宇，
高处不胜寒。'''
    f.write(content)

with open('d:/python_learning/PythonProject_林粒粒呀课程_电脑上/poem.txt', 'a', encoding='utf-8') as f:
    # 下面的content=可以不用，用f.write('''起舞弄清影，\n何似在人间''')
    content = '''
起舞弄清影，
何似在人间。'''
    f.write(content)
