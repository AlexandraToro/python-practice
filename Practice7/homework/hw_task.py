# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.

import os


def rename_files(ext_in: str, ext_out: str, or_range: tuple[int, int], filename="", count=0) -> None:
	files = os.listdir()
	start, end = or_range
	num = 1
	for file in files:
		name, ext = file.split('.')
		if ext == ext_in:
			if len(str(num)) > count:
				print('The counter of files is out of range.')
				break
			else:
				file_num = '0' * (count - len(str(num))) + str(num)
			os.rename(file, (
				name[start - 1: end] if start <= len(
					name) >= end else name) + filename + file_num + f'.{ext_out}')
			num += 1


rename_files('txt', 'test', (1, 3), 'new', 3)
