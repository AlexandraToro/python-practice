# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


class Animal:
	def __init__(self, area):
		self.area = area


class Fishes(Animal):
	def __init__(self, area, add_info):
		self.add_info = add_info
		super().__init__(area)
	
	def __str__(self):
		return f'{type(self).__name__} area = {self.area} info: {self.add_info}'


class Birds(Animal):
	def __init__(self, area, wings):
		self.wings = wings
		super().__init__(area)
	
	def __str__(self):
		return f'{type(self).__name__} area = {self.area} info: {self.wings}'


class Reptiles(Animal):
	def __init__(self, area, info):
		self.info = info
		super().__init__(area)
	
	def __str__(self):
		return f'{type(self).__name__} area = {self.area} info: {self.info}'


class Factory:
	def __new__(cls, *args):
		return args[0](*args[1:])


d = Reptiles("river", "crocodile")
print(d)
c = Factory(Birds, "mountains", "speed wings")
print(c)
