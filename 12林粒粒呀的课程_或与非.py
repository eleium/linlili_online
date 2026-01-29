# and ,or, not 或与非
# and: 全真为真 一假全假！！！  可以多个对象      一损皆损

# or：一真则真  ，全假则假！！！  可以多个对象     一荣皆荣

# not: 反动bool值。 只针对一个对象


# 优先级：  not --> and --> or  闹太套

if (house_work_count > 10 and red_envelope_count > 1 and shopping_count > 1 and not \
        # not 后面的 \ 表示这一行写不下了，再起一行。
    has_been - angry):
    print('摩拳擦掌等待Switch!')
else:
    print('Switch is going with wind!')
# 另起一行的其他写法：在下一行加and
#
# if today_is_wind == True and
#     and my_ex_age > 25 or
#     and my_girl_friend < 25:
