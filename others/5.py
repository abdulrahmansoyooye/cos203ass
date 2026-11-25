class ProductInventory:
    def __init__(self):
        self.__stock = {}
    def add_item(self,name,qty):
       return self.__stock.update({name:qty})
    def sell_item(self,name,qty):
       
       if(product.get_quantity(name) < qty):
        print("Quantity not Available")
       else:
        self.__stock.pop(name,qty)
    def get_quantity(self,name):
       
       return (self.__stock.get(name))
    def __str__(self):
       return "Products in stock: %s" % (self.__stock)
product = ProductInventory()
product.add_item("Bag",12)
product.add_item("Food",12)
product.sell_item("Bag",10)
# stock = product.__stock
print(product)
# print(stock)