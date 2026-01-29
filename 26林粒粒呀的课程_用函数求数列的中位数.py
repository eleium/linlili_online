# median:一个数列的中位数：求中位数是将一组数据按照大小顺序排列后，位于中间位置的数值。

# 如果数据的数量是奇数，中位数就是正中间的那个数；
# 如果数据的数量是偶数，中位数则是中间两个数的平均值。
num_list = [2, 4, 7, 1, -55, 3432, 66, 54]


def median_num_list(num_list):
    new_list = sorted(num_list)
    n = len(new_list)
    if n % 2 == 1:  # n % 2==1表示n 被2除后，余数为1
        print(new_list[n // 2])
        return new_list[n // 2]
    else:
        print((new_list[n // 2 - 1] + new_list[n // 2]) / 2)
        return (new_list[n // 2 - 1] + new_list[n // 2]) / 2


first_list = median_num_list(num_list)
print(first_list)

# 引入模块：  模块名.函数名 或 模块名.变量名。 statistics:统计学的模块包括求平均数，中值等等。
import statistics

print(statistics.median(num_list))

# 第二种方法：
from statistics import median

print(median(num_list))  # 不需要再次写模块名了，直接调用模块中的函数

# 第三种方法：
from statistics import *
# 这是取巧的模式，表示引用了模块statistic中的所有函数。不建议使用。因为可能两个模块有相同的函数名，会混淆。

# 第三方模块先安装 pip install到当地，再从当地模块库引用import或from * import *。python自有模块库可以直接引用。
# 推送到gitee。麻蛋
