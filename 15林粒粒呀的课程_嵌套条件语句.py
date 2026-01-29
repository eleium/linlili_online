# #有时候判断条件不是唯一的，就是嵌套条件语句
# from 林粒粒呀的课程9_判断 import mood_index
#
# if [条件 1 ]：
#     if [条件 2 ]：
#         执行语句     #必须是条件1为真，然后条件2也为真，才 执行本执行语句。
#     else：
#         执行语句# 也可以是多行。 这个else是针对条件2的，条件2为False.
# else：
#     针对条件1，也可以配一个else的语句。
#
# #以上的各行代码必须注意缩进，缩进体现了各个语句的从属，python根据缩进，判断属于哪个分支

# 课程实践：
mood_index = int(input('老婆的心情指数为： '))

if mood_index < 60:
    is_at_home = input("老婆今天是否在家？,请输入'y'或者'n'")  # 注意缩进，表示是在上个if语句里。
    if is_at_home.lower() == 'y':
        print('当心!')
        print('不可以叫上小明一起。')
    else:
        print('今晚放飞自我！')
else:
    print('今晚老实点吧。')
# mood_index = int(input('老婆的心情指数为： '))
# is_at_home = input("老婆今天是否在家？,请输入'y'或者'n'") #这行的位置，不管下面是否<60，都会执行。
#
# if mood_index < 60:
#     if is_at_home.lower() == 'y':
#         print('当心!')
#         print('不可以叫上小明一起。')
#     else:
#         print('今晚放飞自我！')
# else:
#     print('今晚老实点吧。')
