# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# При достижении конца более короткого файла, возвращайтесь в его начало.
import math


def task_3(file1: str, file2: str, file3: str) -> None:
	with (
		open(file1, 'r', encoding="utf8") as f1,
		open(file2, 'r', encoding="utf8") as f2,
		open(file3, 'w', encoding="utf8") as f3):
		num = list(f1)
		nick = list(f2)
		count = max(len(nick), len(num))
		print(count)
		for i in range(count):
			num1 = read_line(f1)
			nick1 = read_line(f2)
			print(num1,nick1)
			a = num1.split("|")
			mult = int(a[0]) * float(a[1])
			if (mult) < 0:
				f3.write(f"{str(nick1.lower())} {round((mult), 0)}\n")
			else:
				f3.write(f"{str(nick1.upper())} {math.fabs(mult)}\n")


def read_line(fd):
	text = fd.readline()
	if text == "":
		fd.seek(0)
		text = fd.readline()
	return text[:-1]


task_3("file1", "file2", "file3")
