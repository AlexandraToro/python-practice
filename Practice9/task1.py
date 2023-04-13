# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного  уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
import random
from typing import Callable

RANGE = 100  # количество строк в csv файле
LOWER_LIMIT = 1  # нижняя граница для рандомного числа
UPPER_LIMIT = 100  # верхняя граница для рандомного числа


def three_numbers(filename: str):
	"""Декоратор, запускающий функцию нахождения корней квадратного  уравнения с каждой тройкой чисел из csv файла."""
	
	def deco(func: Callable):
		def wrapper(*args, **kwargs):
			get_csv_file(filename)
			list_of_roots = []
			with open(filename, 'r', encoding='utf-8') as f:
				reader = csv.reader(f, dialect='excel')
				for i, row in enumerate(reader):
					if row:
						a, b, c = row
						a, b, c, = int(a), int(b), int(c)
						list_of_roots.append(func(a, b, c))
			return list_of_roots
		
		return wrapper
	
	return deco


def save_to_json(func: Callable):
	"""Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл."""
	
	def wrapper(*args, **kwargs):
		with open('roots.json', 'a', encoding='utf-8') as j:
			res = func(*args, **kwargs)
			json.dump(res, j, indent=2)
	
	return wrapper


@save_to_json
@three_numbers('coefficient.csv')
def roots_of_quadratic_equation(a: int, b: int, c: int) -> str:
	"""Решение квадратных уравнений."""
	d = b ** 2 - 4 * a * c
	if d == 0:
		x = (-b) / (2 * a)
		res = f"{x = }"
	elif d > 0:
		x1 = (-b - d ** 0.5) / (2 * a)
		x2 = (-b + d ** 0.5) / (2 * a)
		res = f" res = {x1=}, {x2=}"
	else:
		d: complex = complex(d, 0)
		x1 = (-b - d ** 0.5) / (2 * a)
		x2 = (-b + d ** 0.5) / (2 * a)
		res = f" complex root are {x1=}, {x2=}"
	return res


def get_csv_file(name: str):
	"""Генерация csv файла с тремя случайными числами в каждой строке 100-1000 строк."""
	with open(name, "w", encoding='utf8') as c:
		writer = csv.writer(c, dialect='excel', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for _ in range(RANGE + 1):
			line = []
			for i in range(3):
				line.append(random.randint(LOWER_LIMIT, UPPER_LIMIT))
			writer.writerow(line)


if __name__ == '__main__':
	roots_of_quadratic_equation()
