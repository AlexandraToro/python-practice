import logging


class Foursquare:
	
	def __init__(self, a, b=0):
		FORMAT = '{levelname:<8} - {asctime}. {msg}'
		logging.basicConfig(format=FORMAT, style='{', filename='foursquare.log.', filemode='a', encoding='utf-8',
		                    level=logging.INFO)
		self.logger_f = logging.getLogger(__name__)
		self.a = a
		if b == 0:
			self.b = a
		else:
			self.b = b
		self.logger_f.info(f'Foursquare with sides {self.a}, {self.b} formed')
	
	def get_length(self):
		self.logger_f.info('Calculated the perimeter of the foursquare')
		return 2 * self.a + 2 * self.b
	
	def get_square(self):
		self.logger_f.info('Calculated the square of the foursquare')
		return self.a * self.b
	
	def __add__(self, other):
		a = (self.get_length() + other.get_length()) / 4
		return Foursquare(a)
	
	def __sub__(self, other):
		if self.get_length() < other.get_length():
			self.logger_f.error('Calculation is not possible, the subtracted rectangle is larger than the original')
			raise Exception("Calculation is not possible, the subtracted rectangle is larger than the original")
		else:
			a = (self.get_length() - other.get_length()) / 4
			return Foursquare(a)
	
	def __str__(self):
		if self.b == 0 or self.a == self.b:
			return f'Прямоугольник является квадратом со стороной {self.a}'
		else:
			return f'Стороны прямоугольника {self.a} и {self.b}'
