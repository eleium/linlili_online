# str.formate() 格式化字符串的一个强大的工具：调用方法：
string = '{} is a {} programing language.'.format('python', 'popular')
print(string)
# {}是占位符，format('python','popular')是两个要被依次传进去的参数。*args

string = '{0} is a {1} programing language.'.format('python', 'popular')
# 花括号里面可以带上索引的占位符，明确format的参数传递的顺序。

contacts = ['小李', '小王', '小赵', '小钱', '小张']
year = '虎'
name = contacts

for name in contacts:
    message_content ='''
(律回春渐，新元肇启，\n
新岁甫至，福气东来。\n
金{0}敲门，五福临门。\n
给{1}及家人拜年啦！\n
新春快乐，{0}年大吉！)'''.format(year, name)
    print(message_content)

gpa_dictionary={'小明':38,'小花':44,'小亮':90,'小李':23}
for name,gpa in gpa_dictionary.items():
    print(f'{0}你的绩点是{1},请保持')
    print('{0}你的绩点是{1},请保持'.format(name,gpa))

#f-string 中用花括号 {} 时，里面应该是变量名或表达式，比如 {name} 或 {gpa}，
# 而不能写数字索引 {0}、{1}（那是 .format() 的用法）。
# 你这里想表达的是用 name 和 gpa 变量填充字符串，所以应该写成：
# f'{name}你的成绩点是{gpa}，请保持。