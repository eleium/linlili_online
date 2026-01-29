# import math 引入模块
# 一个数列,求数列的和
number_list = [23, 555, 6, 7042]

def sum_list_1(number_list):
    # 定义函数时括号内要和调用时传入的参数一致
    # 如果括号空，调用时也不要传参数
    # 如果括号内有参数，调用时必须传对应的 参数：sum_list_1(some_list)
    result = 0
    for num in number_list:  # for语句是循环语句，遍历列表中的每一项。与if 语句完全不同。if是判断。
        result += num
    print(result)
    #注意缩进，不要缩在for语句内，那么就不是def的内容了。
    #更推荐不要在这里写print，在传入参数后，验证时再写print().
    return result

sum_list_1(number_list)  # 调用参数

