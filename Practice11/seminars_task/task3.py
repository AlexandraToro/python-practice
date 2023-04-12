# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

class Foursquare:
	"""
	Класс принимает стороны прямоугольника, вычисляет его периметр и площадь.
	Имеются методы сложения, вычитания и сравнения прямоугольников.
	"""
	
	def __init__(self, a, b=0):
		"""
		Добавлены параметры a и b
		"""
		self.a = a
		if b == 0:
			self.b = a
		else:
			self.b = b
	
	def get_length(self):
		"""вычисляет периметр прямогуольника"""
		return 2 * self.a + 2 * self.b
	
	def get_square(self):
		"""вычисляет площадь прямогуольника"""
		return self.a * self.b
	
	def __add__(self, other):
		"""Сложение прямоугольников"""
		a = (self.get_length() + other.get_length()) / 4
		return Foursquare(a)
	
	def __sub__(self, other):
		"""Вычитание прямоугольников"""
		if self.get_length() < other.get_length():
			raise Exception("Вычисление невозможно")
		else:
			a = (self.get_length() - other.get_length()) / 4
			return Foursquare(a)
	
	def __str__(self):
		"""Представлени экземпляров"""
		if self.b == 0 or self.a == self.b:
			return f'Прямоугольник является квадратом со стороной {self.a}'
		else:
			return f'Стороны прямоугольника {self.a} и {self.b}'
	
	def __eq__(self, other):
		"""Равны ли прямоугольники"""
		x = self.get_square()
		y = other.get_square()
		return x == y
	
	def __gt__(self, other):
		"""Сравнение больше"""
		x = self.get_square()
		y = other.get_square()
		return x > y
	
	def __ge__(self, other):
		"""Сравнение меньше или равно"""
		x = self.get_square()
		y = other.get_square()
		return x <= y
	
	def __lt__(self, other):
		"""Сравнение меньше"""
		x = self.get_square()
		y = other.get_square()
		return x < y
	
	def __le__(self, other):
		"""Сравнение больше или равно"""
		x = self.get_square()
		y = other.get_square()
		return x >= y


n = Foursquare(5, 8)
print(n.get_length())
m = Foursquare(4, 6)
print(m.get_length())
print(n + m)
print(n - m)
# print(m - n)
print(m.get_square(), "\n", n.get_square())
print(f"m == n {m == n}")
print(f"m != n {m != n}")
print(f"m > n {m > n}")
print(f"m < n {m < n}")
print(f"m >= n {m >= n}")
print(f"m <= n {m <= n}")
help(Foursquare)