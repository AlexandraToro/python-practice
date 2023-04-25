import unittest
from circle import Circle
from circle_exception import NotNumException


class CircleTest(unittest.TestCase):
	
	def setUp(self) -> None:
		self.circle = Circle(5)
		
	def test_perimeter(self):
		self.assertEqual(self.circle.get_perimeter(), 31.42)
		
	def test_square(self):
		self.assertEqual(self.circle.get_square(), 78.54)
		
	def test_value_error(self):
		self.assertRaises(NotNumException, Circle, 'five')
		
	def test_negative_value(self):
		self.assertEqual(Circle(-2).get_square(), 12.57)
		
		
if __name__ == '__main__':
	unittest.main(verbosity=2)