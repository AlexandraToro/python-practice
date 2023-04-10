import json


def json_writer(input_dict: [list, dict], filename: str) -> None:
	"""
	Запись в json файл
	:param input_dict: словарь с данными для записи
	:param filename: название файла для записи
	"""
	filename = f"{filename}.json"
	with open(filename, 'w', encoding='utf-8') as j:
		json.dump(input_dict, j, indent=4)
