# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей
# в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
import random

N = 8
MAX_SUCCESSFUL_COORD = 4


def task_about_8queens(coord: list[int]) -> bool:
	x = []
	y = []
	for i in range(len(coord)):
		x.append(coord[i] // 10)
		y.append(coord[i] % 10)
	for i in range(N):
		for j in range(i + 1, N):
			if abs(x[i] - x[j]) == abs(y[i] - y[j]):
				return False
			else:
				return True


def get_random_coord() -> list[int]:
	list_ = []
	list_x = []
	list_y = []
	while len(list_) < N:
		num = random.randint(11, 88)
		x = num // 10
		y = num % 10
		if num not in list_ and x not in list_x and y not in list_y and y != 0 and y != 9:
			list_x.append(num // 10)
			list_y.append(num % 10)
			list_.append(num)
	return list_


if __name__ == '__main__':
	check = 0
	print("Successful coordinates: ")
	while check < MAX_SUCCESSFUL_COORD:
		array = get_random_coord()
		if task_about_8queens(array):
			print(array)
			check += 1
