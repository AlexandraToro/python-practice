import csv


def csv_writer(input_dict: [list, dict], filename: str) -> None:
	"""
	Запись в csv-файл
	:param input_dict: данные на запись
	:param filename: название файла
	"""
	filename = f"{filename}.csv"
	with open(filename, 'w', encoding='utf-8') as c:
		write_csv = csv.writer(c, dialect='excel', delimiter='\n')
		write_csv.writerow(input_dict)