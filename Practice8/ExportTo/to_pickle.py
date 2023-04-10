import pickle


def pickle_writer(input_data: dict, filename) -> None:
	"""
	Программа записывает данные в файл в виде потока байт при помощи модуля pickle
	:param input_data: данные для перевода
	:param filename: название файла для записи
	"""
	filename = f"{filename}.pickle"
	with open(filename, "wb") as p:
		pickle.dump(input_data, p)
