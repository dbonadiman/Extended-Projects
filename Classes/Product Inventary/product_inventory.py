class Product:
	__id = -1
	__price = -1.0
	__quantity = -1

	def __init__(self, id, price, quantity):
		self.__id=id
		self.__price=price
		self.__quantity=quantity

	def price(self):
		return self.__price

	def quantity(self):
		return self.__quantity

	def add_quantity(self,quantity):
		self.__quantity += quantity

	def id(self):
		return self.__id

class Inventory:
	__products = []
	def __init__(self, products =[]):
		self.__products+=products

	def add_product(self,p):
		for prod in self.__products:
			if p.id() == prod.id():
				prod.add_quantity(p.quantity())
				return
		self.__products.append(p)

	def total_price(self,total=0):
		for p in self.__products:
			total += p.quantity()*p.price()
		return total




def main():
	inventory = Inventory()
	inventory.add_product(Product(1,15.0,2))
	inventory.add_product(Product(2,13.0,1))
	inventory.add_product(Product(1,15.0,1))
	print inventory.total_price()

if __name__=="__main__":
	main()