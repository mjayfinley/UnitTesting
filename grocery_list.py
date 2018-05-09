class ShoppingList:
    def __init__(self):
        self.list = []
        self.items = []

    def add_list(self,store):
        self.list.append(store)

    def add_items(self,items):
        self.items.append(items)

list_one = ShoppingList()
list_two = ShoppingList()
list_three = ShoppingList()

list_one.add_list('Walmart')
list_one.add_items('eggs')
list_one.add_items('bread')
list_one.add_items('milk')


list_two.add_list('Kroger')
list_two.add_items('fruit')
list_two.add_items('steak')
list_two.add_items('veggies')


list_three.add_list('HEB')
list_three.add_items('butter')
list_three.add_items('lettuce')
list_three.add_items('juice')



print(f"Your {list_one.list} list is: {list_one.items}")
print(f"Your {list_two.list} list is: {list_two.items}")
print(f"Your {list_three.list} list is: {list_three.items}")
