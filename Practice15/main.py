import argparse
from circle import Circle
from foursquare import Foursquare


def prog():
	args = argparse.ArgumentParser()
	args.add_argument("-f", "--figure", help='Enter the shape of the figure "circle" or "foursquare"')
	args.add_argument("-v", "--value", help='Enter radius or side of foursquare', default=1)
	args.add_argument("-s", "--side", help='Enter the second side of foursquare', default=0)
	arg_res = args.parse_args()
	if arg_res.figure == "circle":
		a = Circle(arg_res.value)
		print(a.get_square())
	elif arg_res.figure == "foursquare":
		a = Foursquare(arg_res.value, arg_res.side)
		print(a.get_square())
		print(a.get_length())


if __name__ == '__main__':
	prog()
