# Задание No1
# 📌 Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str
# 📌 дополнительно хранятся имя автора строки и время создания
# (time.time)


class MyStr(str):
	"""Класс наследуется от str с дополнительными свойствами хранения имя автора и времени создания"""
	
	def __new__(cls, autor, value):
		from time import time
		instance = super().__new__(cls, value)
		instance.autor = autor
		instance.time = time()
		return instance
	
	def __str__(self):
		return f"{self = } \n{self.autor =} \n{self.time =}"


a = MyStr("DFVdf", "string123")
print(a)
print(a.upper())
print(a.autor)
