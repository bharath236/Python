class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self,item_name,quantity):
        self.items[item_name] = quantity

    def get_items(self):
        print(self.items)

    def remove_item(self,item_name):
        del self.items[item_name]
        
    def update_quantity(self,item_name, quantity):
        self.items[item_name] = quantity

cart_obj = Cart()
cart_obj.add_item("book",10)
cart_obj.get_items()
cart_obj.add_item("macbook",2)
cart_obj.get_items()
cart_obj.remove_item("book")
cart_obj.get_items()
cart_obj.update_quantity("book",23)
cart_obj.get_items()