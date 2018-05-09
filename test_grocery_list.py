import unittest
from grocery_list import ShoppingList

class TestShoppingList(unittest.TestCase):

    def setUp(self):
        self.shoppinglist = ShoppingList()

    def test_add_list(self):
        result = self.shoppinglist.add_list('Walmart')
        self.assertTrue('x',result)


    def test_add_items(self):
        result = self.shoppinglist.add_items('eggs')
        self.assertTrue('y',result)


if __name__ == '__main__':
    unittest.main()
