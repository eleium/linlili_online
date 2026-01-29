'''
assertEqual,测试是否为真，如果相等即为True,测试通过。
方法的结果类似于后者。
assertEqual(a, b) - -->  assert a == b
assertTrue(a) - -->assert a == True
asertIN(a, b) - -->assert a in b

assertNotEqual(a,b) --->assert a !=b
assertFalse(a) --->assert a=False
assertNotIn(a,b) --->assert a not in b
'''

# assertTrue(2 not in [1,3,-4]) ====-> assertNOtIn (2,[1,3,-4])
# 前者可以广泛使用，是万能方法。后者针对性更强，更易懂。如果没通过，后者会给出更具体的原因。


'''
有时候要测试一个类，就要创建类的实例来带入，如果要测试不同的错误类型，就要重复的输入实例。
这时候，可以用TestCase类里面的setUp方法来避免重复的输入实例类的代码。
在运行各个测试，也就是test_开头的语句前，创建类的一个叫setUp的属性，都会被运行一次。
'''
class Sentence:#定义一个类,一句话或一句文本的类。
    def __init__(self,sentence):#这个类有属性：sentence
        self.sentence=sentence#传入的参数将作为这个类的属性。

    def letter_count(self):#定义一个 统计字母的函数
        return len(self.sentence)
    def word_count(self):#定义一个 单词数量的函数
        return len(self.sentence.split(''))
    def upper(self):#返回所有字母大写后的句子
        return self.sentence.upper()

import unittest
from sentence import Sentence
class TestSentence(unittest.TestCase):
    def setUp(self):
        self.sentence=Sentence('hello world!')

    def test_str_count(self):
        self.assertEqual(self.sentence.str_count(),12)
    def test_word_count(self):
        self.assertEqual(self.sentence.word_count(),2)
    def test_upper(self):
        self.assertEqual(self.sentence.upper(),'HELLO  WORLD!')