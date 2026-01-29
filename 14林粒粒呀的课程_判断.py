# 判断语句 if then
'''
判断语句的格式：  if [条件】：  (只要是bool值就可以）
                            其中的条件可以是  True  或者   False，比如：
                            today_is_good=True,就可以写成：  if[today_is_good]:
也可以用比较符：  >,>=， <,<=,  ==, !=   .如： 3==3--> True   'a'=='b'-->False

如： if [5>20]:     因为5>20返回值是False,所以可以用来判断。

'''
# from 林粒粒呀课程3 import my_ex

my_name = 'elei'

if my_name == 'elei':
    print(my_name)  # 条件为真的时候的执行语句
    # 可以有多行执行语句

else:  # 条件为假False时的执行语句，也可以为多行执行语句。
    print('ok')

# 课堂实践：

mood_index = int(input('老婆今晚的心情指数是： '))#别忘了，input返回的是字符串，不能比较，所以先int。
if mood_index >= 60:
    print("恭喜啦，今晚可以打游戏了！")

else:
    print('今晚老实点吧！')
