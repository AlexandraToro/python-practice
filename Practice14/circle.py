import math
from circle_exception import NegativeValueException, NotNumException


class Circle:

	def __init__(self, radius):
		if isinstance(radius, int):
			self.radius = radius
		else:
			raise NotNumException
		try:
			if self.radius < 0:
				raise NegativeValueException(self.radius)
		except NegativeValueException as e:
			print(e)
			self.radius = abs(self.radius)
	
	def get_perimeter(self):
		return round(2 * math.pi * self.radius, 2)
	
	def get_square(self):
		return round(math.pi * (self.radius ** 2),2)

if __name__ == '__main__':
	Circle(" ")