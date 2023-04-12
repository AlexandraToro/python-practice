# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

class Archive:
	"""
	Класс хранит пару свойств. При нового экземпляра класса,
	старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов.
	"""
	_instance = None
	
	def __new__(cls, *args, **kwargs):
		"""
		Сохраняет данные из ранее созданных экземпляров в list-архивов.
		"""
		if cls._instance is None:
			cls._instance = super().__new__(cls)
			cls._instance.list_text = []
			cls._instance.list_num = []
		else:
			cls._instance.list_text.append(cls._instance.text)
			cls._instance.list_num.append(cls._instance.number)
		return cls._instance
	
	def __init__(self, text, number):
		"""Добавляет свойства текст и число."""
		self.text = text
		self.number = number
	
	def __str__(self):
		"""Переропределение метода представления класса"""
		return f"Экземпляр класса Archive хранит строку {self.text} и число {self.number}.\n" \
		       f"Ранее сохранено {self.list_num} & {self.list_text}"
	
	def __repr__(self):
		"""Переропределение метода представления класса ждя разработчиков"""
		return f"Archive({self.text}, {self.number})"


if __name__ == '__main__':
	a = Archive("hgv", 5)
	print(a.list_text,a.list_num)
	b = Archive("fbdv", 45)
	print(b.list_text, b.list_num)
	c = Archive("vbhj",765)
	print(b.list_text, b.list_num)
	help(Archive)
	print("______________________")
	print(c)
	print("______________________")
	print(f'{c}')
	print("______________________")
	print(repr(c))
	d = repr(c)
	print(d)
	print("______________________")
	print(f'{c = }')
