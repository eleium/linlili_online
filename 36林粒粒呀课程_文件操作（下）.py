# 写文件的时候，如果文件名不存在，就会创建一个文件
with open('d:/python_learning/PythonProject_林粒粒呀课程_电脑上/new_file.txt',
          'w', encoding='utf-8') as f1:
    content = '''
    白日依山尽，
    黄河入海流。
    欲穷千里目，
    更上一层楼。
少小离家老大归，
乡音未改鬓毛衰。
    '''
    f1.write(content)  # 这是with语句的写入方法。也要缩进。
    f1.write('今天是个好日子')  # 此时with语句未结束，故文件内容没覆盖而是续写。

# 用参数'a'来在原来的文件里追加写操作.与'w'操作一样，如果原文不存在，就会创作一个文件。
with open('d:/python_learning/PythonProject_林粒粒呀课程_电脑上/new_file.txt',
          'a', encoding='utf-8') as f:
    f.write('\nwhat a beautiful cat!')  # 要让追加的在下一行显示，在句子前就加 \n

#用'r+"的方法，可以直接阅读。   ###这不是追加！！！！！！是从头加入，但不覆盖

with open('./new_file.txt','r+',encoding='utf-8') as f:
    f.write('燕山雪花大如席')
    print(f.read())


