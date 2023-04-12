# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

class Matrix:
	"""
	Создает матрицы, выводит на экран, сожержит методы сравнения, сложения, умножения матриц.
	"""
	
	def __init__(self, matrix: list[list[int]]):
		"""
		Инициация матрицы
		:param matrix: матрица
		"""
		self.matrix = matrix
		self.rows = len(matrix)
		self.columns = len(matrix[0])
	
	def compare_size(self, other):
		"""Сравнение размеров матриц"""
		return len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0])
	
	def __add__(self, other):
		"""Сложение матриц"""
		if self.compare_size(other):
			new = [[None for _ in range(self.columns)] for _ in range(self.rows)]
			for i in range(self.rows):
				for j in range(self.columns):
					new[i][j] = self.matrix[i][j] + other.matrix[i][j]
			return new
		else:
			raise Exception("Сложение матриц возможно при равных длине и ширине")
	
	def __mul__(self, other):
		"""Умножение матриц"""
		if len(self.matrix[0]) == len(other.matrix):
			m, n = len(self.matrix), len(other.matrix[0])
			multi_result = [[0 for _ in range(n)] for _ in range(m)]
			for i in range(m):
				for j in range(n):
					for k in range(len(other.matrix)):
						multi_result[i][j] += self.matrix[i][k] * other.matrix[k][j]
			return multi_result
		else:
			raise Exception("Умножение матриц возможно при равенстве количества столбцов первой матрицы"
			                " количеству строкам второй матрицы. ")
	
	def __eq__(self, other):
		"""Равенство матриц"""
		if self.compare_size(other):
			for i in range(self.rows):
				for j in range(self.rows):
					if self.matrix[i][j] == other.matrix[i][j]:
						return True
					else:
						return False
		else:
			return False
	
	def __ne__(self, other):
		"""Неравенство матриц"""
		if self.compare_size(other):
			for i in range(self.rows):
				for j in range(self.rows):
					if self.matrix[i][j] != other.matrix[i][j]:
						return True
					else:
						return False
		else:
			return False
	
	def __str__(self):
		"""Вывод матрицы для пользователя"""
		return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix]) + '\n'
	
	def __repr__(self):
		"""Вывод для разработчика"""
		return f'Matrix({self.matrix})'


if __name__ == '__main__':
	a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
	b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
	c = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
	print("Matrix A: ")
	print(a)
	print(f'Matrix B: \n{b}')
	print(f'Matrix C: \n{c}')
	print(repr(b))
	print(f'{c = }')
	print(f'Размер матрицы А равна размеру матрицы С: {c.compare_size(a)}')
	print(f'Сумма матриц А и B равна: \n{a + b}')
	print(f'Произведение матриц А и С равно : \n{a * c}')
	print(f'Матрица А равна матрице B: {a == b}')
	print(f'Матрица А не равна матрице B: {a != b}')
	help(Matrix)
