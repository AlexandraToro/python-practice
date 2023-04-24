class CircleException(BaseException):
	def __init__(self, name, message):
		self.name = name
		self.msg = message
		
	def __str__(self):
		return (f'ERROR...\n{self.name} : {self.msg}')


class NegativeValueException(CircleException):
	def __init__(self, value):
		super().__init__('NegativeValueException',
		                 f'Radius can not be negative. For the radius will take the modulus of the entered number "{value}"')
		

class NotNumException(CircleException):
	def __init__(self):
		super().__init__('NotNumException', 'Entering a numeric value is required...')

		