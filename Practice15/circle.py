import math
import logging


class Circle:
	def __init__(self, radius):
		FORMAT = '{levelname:<8} - {asctime}. {msg}'
		logging.basicConfig(format=FORMAT, style='{', filename='circle.log.', filemode='a', encoding='utf-8',
		                    level=logging.INFO)
		self.logger = logging.getLogger(__name__)
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
		self.logger.info(f'Circle with radius = {self.radius} object formed')
	
	def get_perimeter(self):
		self.logger.info('Calculated the perimeter of the circle')
		return round(2 * math.pi * self.radius, 3)
	
	def get_square(self):
		self.logger.info('Сalculated the square of the circle')
		return round(math.pi * (self.radius ** 2), 3)


class CircleException(BaseException):
	def __init__(self, name, message):
		FORMAT = '{levelname:<8} - {asctime}. {msg}'
		logging.basicConfig(format=FORMAT, style='{', filename='circle.log.', filemode='a', encoding='utf-8',
		                    level=logging.INFO)
		self.logger = logging.getLogger(__name__)
		self.name = name
		self.msg = message
	
	def __str__(self):
		self.logger.error(f'ERROR...{self.name} : {self.msg}')
		return (f'ERROR...\n{self.name} : {self.msg}')


class NegativeValueException(CircleException):
	def __init__(self, value):
		super().__init__('NegativeValueException',
		                 f'Radius can not be negative. For the radius will take the modulus of the entered number "{value}"')


class NotNumException(CircleException):
	def __init__(self):
		super().__init__('NotNumException', 'Entering a numeric value is required...')

