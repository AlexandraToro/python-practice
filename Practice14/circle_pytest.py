import pytest
from circle import Circle
from circle_exception import NotNumException


@pytest.fixture()
def circle():
	return Circle(5)


def test_perimeter(circle):
	assert circle.get_perimeter() == 31.42


def test_square(circle):
	assert circle.get_square() == 78.54


def test_value_error():
	with pytest.raises(NotNumException):
		Circle('five')


def test_negative_value():
	assert Circle(-2).get_square() == 12.57


if __name__ == '__main__':
	pytest.main()
