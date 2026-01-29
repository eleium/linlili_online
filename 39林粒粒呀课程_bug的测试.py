"""如何测试bug  assert(断言),它后面可以是任何bool表达式： True or False,测试时，我们在assert的
后面跟上我们认为是 True的表达式.如果表达式结果为True，程序继续执行。如果表达式运行的结果是False，
就会报错： AssertionError:断言错误,程序就此中止，不再运行。
可以用python中的一个unittest单元测试库，可以一次性跑多个测试。可以对最小的可测试单元进行测试
import unittest
"""

assert len('Hi') == 2
assert 1 + 2 > 6
assert "a" in ["c", "b"]

def my_adder(a,b):
    return a+b
def my_calculator(c,d):
    return c*d

import unittest

from my_calculator import my_adder#格式： from 文件名import 函数名或类名（这是在同一个文件夹下）

class TestMyAdder(unittest.TestCase):
    def test_positive_with_positive(self):
        self.assertEqual(my_adder(5,3),8)
    def test_negative_with_positive(self):
        self.assertEqual(my_adder(-5,3),2)

###这一章是学的最差的，啥都没搞明白
#怎么使用，是在所有程序之前加try assert finally啥的还是在程序中开始测试？
#test到底怎么用？他的语法，格式啥意思？
#unittest 单元测试 导入后，如何与test一起使用？
