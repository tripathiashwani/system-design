class MenuItem:
	def __init__(self, code, name, price):
		self.__code = code
		self.__name = name
		self.__price = price

	def get_code(self):
		return self.__code

	def get_name(self):
		return self.__name

	def get_price(self):
		return self.__price
