import random
from typing import Callable


def deco(func: Callable):
	MIN_NUM = 1
	MAX_NUM = 100
	MIN_COUNT = 1
	MAX_COUNT = 10
	
	def wrapper(num1: int, num2: int, *args, **kwargs):
		if num1 not in range(MIN_NUM, MAX_NUM):
			num1 = random.randint(MIN_NUM, MAX_NUM)
		if num2 not in range(MIN_COUNT, MAX_COUNT):
			num2 = random.randint(MIN_NUM, MAX_NUM)
		return func(num1, num2)
	
	return wrapper


@deco
def view_game(a: int, b: int):
	for i in range(1, b):
		c = int(input("Enter your number: "))
		if c == a:
			print("U win!")
			break
		elif a > c:
			print("загаданное число больше")
		else:
			print("загаданное число меньше")
	else:
		print(f"Failed, number is {a}, attempts {b}")
		return


if __name__ == '__main__':
	game = view_game(99, 5)
	game()
