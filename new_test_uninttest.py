import unittest
from example_shopping_list import ShoppingList

class TestShoppingList(unittest.TestCase):
    # 初始化方法 (每个测试方法前执行)
    def setUp(self):
        self.shopping_list = ShoppingList({
            '纸巾': 8,
            '帽子': 30,
            '拖鞋': 15
        })

    # ✅ 测试方法必须缩进在类内部
    def test_get_item_count(self):
        self.assertEqual(self.shopping_list.get_item_count(), 3)

    # ✅ 测试方法命名需以test_开头
    def test_get_total_price(self):
        self.assertEqual(self.shopping_list.get_total_price(), 53)

    # 建议添加空购物清单测试
    def test_empty_list(self):
        empty = ShoppingList({})
        self.assertEqual(empty.get_item_count(), 0)
        self.assertEqual(empty.get_total_price(), 0)

if __name__ == '__main__':
    unittest.main()