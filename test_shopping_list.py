# 要测试一个程序，先新开一个文件
# 导入单元测试模块
import unittest

# 从文件名为example_shopping_list的文件中导入ShoppingList类
from example_shopping_list import ShoppingList


# 新建一个类,让它继承unittest库里面的TestCase类
class TestShoppingList(unittest.TestCase):

    # 先测试get_item_count(计算购物清单物品）
    def test_get_item_count(self):
        # 导入ShoppingList类的属性
        shopping_list = ShoppingList({'纸巾': 8, '帽子': 30, '拖鞋': 15})
        # 断言这个集合里面 的商品项目为3
        self.assertEqual(shopping_list.get_item_count(), 3)

    def test_get_total_price(self):
        # 还是调用ShoppList的属性，也就是这个类的购物清单
        shopping_list = ShoppingList({'纸巾': 8, '帽子': 30, '拖鞋': 15})
        self.assertEqual(shopping_list.get_total_price(), 53)  # price后面要有()，因为是调用的方法
    # #

    # 因为重复创建  shopping_list=ShoppingList({'纸巾':8,'帽子':30,'拖鞋':15})
    # 可以用setUp方法
    # 上面的注释不能用''' '''，只能用#


#
#     def setUp(self):
#         self.shopping_list = ShoppingList({'纸巾': 8, '帽子': 30, '拖鞋': 15})
#
#
# # 那么上面的程序可以写成：
#     def test_get_item_count(self):
#         self.assertEqual(self.shopping_list.get_item_count(), 3)
#
#
#     def test_total_price(self):
#         self.assertEqual(self.shopping_list.get_total_price(), 53)

