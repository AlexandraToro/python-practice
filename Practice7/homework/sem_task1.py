# апишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# # Количество строк и имя файла передаются как аргументы функции.
import random

LIMIT = 1000


def num_file(count: int, file_name: str) -> None:
	with open(file_name, 'a', encoding='utf8') as f:
		for i in range(count):
			r1 = random.randint(-LIMIT, LIMIT)
			r2 = random.uniform(-LIMIT, LIMIT)
			print(f"{r1}|{r2}", file=f)


num_file(5, "file1")
