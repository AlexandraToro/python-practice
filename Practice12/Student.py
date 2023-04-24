# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.


import csv
from random import randint


class CheckName:
	def __set_name__(self, owner, name):
		self.param_name = '_' + name
	
	def __get__(self, instance, owner):
		return getattr(instance, self.param_name)
	
	def __set__(self, instance, value):
		if value.isalpha and value.istitle:
			setattr(instance, self.param_name, value)
		else:
			raise ValueError(
				'Last name and first name must be alphabetic and start with a capital letter.')


class Student:
	first_name = CheckName()
	last_name = CheckName()
	
	def __init__(self, first_name: str, last_name: str, subject: str):
		self.first_name = first_name
		self.last_name = last_name
		self.marks = {}
		self.test_result = {}
		self.subject = []
		with open(subject, 'r', newline='', encoding='utf8') as s:
			csv_read = csv.reader(s, 'excel')
			for line in csv_read:
				self.subject = line
		for i in self.subject:
			count_marks = randint(1, 10)
			list_marks = [randint(2, 5) for j in range(count_marks)]
			list_tests = [randint(0, 100) for j in range(count_marks)]
			self.marks[i] = list_marks
			self.test_result[i] = list_tests
	
	def __str__(self):
		return f'First Name: {self.first_name}, Last Name: {self.last_name}. \n' \
		       f'Average score in all subjects = {self.average_marks()}, \n' \
		       f'Average test score for each subject: {self.average_tests()}.'
	
	def average_marks(self) -> float:
		res = 0
		count = 0
		for value in self.marks.values():
			res += sum(value)
			count += len(value)
		return round(res / count, 2)
	
	def average_tests(self) -> dict:
		new_dict = {}
		for key, value in self.test_result.items():
			new_dict[key] = round(sum(value) / len(value), 2)
		return new_dict


if __name__ == '__main__':
	a = Student('Harry', 'Potter', 'subjects.csv')
	print(a)
