# Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.
import os
import random
import string


def do_file(ext, min_len=6, max_len=30, min_byte=256, max_byte=4096, count=42):
	letters = string.ascii_lowercase
	for i in range(count):
		name = f"{''.join(random.choice(letters) for i in range(min_len, max_len))}.{ext}"
		text = ''.join(random.choice(letters) for i in range(min_byte, max_byte))
		with open(name, 'a', encoding="utf8") as f:
			f.write(text)


do_file("txt", count=3)
