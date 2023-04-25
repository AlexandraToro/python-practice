from Practice14.circle import Circle


def circle_doc():
	"""
	>>> print(Circle(5).get_perimeter())
	31.42
	>>> print(Circle(5).get_square())
	78.54
	>>> Circle('five')
	Traceback (most recent call last):
	...
	Practice13.circle_exception.NotNumException: ERROR...
	NotNumException : Entering a numeric value is required...
	>>> Circle(' ')
	Traceback (most recent call last):
	...
	Practice13.circle_exception.NotNumException: ERROR...
	NotNumException : Entering a numeric value is required...
	>>> Circle(-2).get_square()
	ERROR...
	NegativeValueException : Radius can not be negative. For the radius will take the modulus of the entered number "-2"
	12.57
	>>> Circle()
	
	"""


if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)