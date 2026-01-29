#用循环来做一个问候短语，每个人的名字不同。

contacts=['小李','小王','小赵','小钱','小张']
for name in contacts:
    message=(name+'你好，新年庚始，\n万象更新。\n祝'+name+'全家节日快乐！')
    print(message)
# new_message=('''
# 律回春渐，新元肇启，
# 新岁甫至，福气东来。
# 金x贺岁，欢乐祥瑞，
# 金x敲门，五福临门。
# 给xx及家人拜年啦！
# 新春快乐，x年大吉！
# ''')

year='虎'
new_message=('''
律回春渐，新元肇启，
新岁甫至，福气东来。
金+year+贺岁，欢乐祥瑞，
金+year+敲门，五福临门。
给+contacts+及家人拜年啦！
新春快乐，+year+年大吉！
''')

print(new_message)
