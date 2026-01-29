num_list = [88, 23, 4454, -5402, 4149]


# 定义一个求和函数：
def total(num_list):  # 函数定义：定义了一个名为 total 的函数，该函数接受一个列表 num_list 作为参数。
    result = 0  # 初始化 result：在函数内部，将 result 初始化为 0，用于存储累加的结果。
    for num in num_list:  # 遍历列表并累加：使用 for 循环遍历列表中的每个元素，将其累加到 result 中。
        result += num
    return result  # 返回结果：循环结束后，使用 return 语句返回累加的结果。


total_1 = total(num_list)  # 调用函数并打印结果：在函数外部调用 total 函数，并将 num_list 作为参数传递给它，
# 将函数的返回值存储在 total_result 变量中，最后打印该结果。。
print(total_1)
average_total = total_1 / 2  # average:平均值的意思
print(average_total)
