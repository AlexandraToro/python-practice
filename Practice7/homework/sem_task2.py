# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# Полученные имена сохраните в файл.


import random
import string


def get_name(count: int, file_name: str) -> None:
	with open(file_name, 'w', encoding='utf8') as f:
		for i in range(count):
			length = random.randint(4, 7)
			letters = string.ascii_lowercase
			nick = ''.join(random.choice(letters) for i in range(length)).capitalize()
			print(nick)
			if "aouyei" in nick:
				f.write(f"{nick}\n")


get_name(5, "file2")
