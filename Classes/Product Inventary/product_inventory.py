class Product:
    _id = -1
    _price = -1.0
    _quantity = -1

    def __init__(self, id, price, quantity):
        self._id=id
        self._price=price
        self._quantity=quantity
        
    def __hash__(self):
        return hash(self._id)

    def price(self):
        return self._price

    def quantity(self):
        return self._quantity

    def add_quantity(self,quantity):
        self._quantity += quantity

    def id(self):
        return self._id


class Inventory:
    _products = []
    def __init__(self, products = None):
        if products is None:
            products = []
        self._products+=products
    
    #!!! PERFORMANCE: more performance needed.
    def add_product(self,p):
        if p in self._products:
            self._products[self._products.index(p)].add_quantity(p.quantity())
        else:
            self._products.append(p)

    def total_price(self):
        return sum(p.quantity()*p.price() for p in self._products)


def main():
    inventory = Inventory()
    inventory.add_product(Product(1,15.0,2))
    inventory.add_product(Product(2,13.0,1))
    inventory.add_product(Product(1,15.0,1))
    print(inventory.total_price())

if __name__=="__main__":
    main()