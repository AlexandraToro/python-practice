# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import ExportTo
import os


def get_info(folder_path: str) -> None:
	info = {}
	for path, dir_name, file_name in os.walk(folder_path):
		list_dir = os.listdir(path)
		for i in list_dir:
			if os.path.isdir(path + '\\' + i):
				info[i] = {'type': 'dir'}
				size = 0
				for j in os.scandir(path + '\\' + i):
					size += os.stat(j).st_size
				info[i]['size'] = str(size)
				info[i]['parent_folder'] = path.split('\\')[-2]
			elif os.path.isfile(path + '\\' + i):
				info[i] = {'type': 'file'}
				info[i]['size'] = str(os.path.getsize(path + '/' + i))
				info[i]['parent_folder'] = path.split('\\')[-1]
	ExportTo.pickle_writer(info, "pickle_file")
	ExportTo.json_writer(info, "json_file")
	ExportTo.csv_writer(info, "csv_file")


get_info('C:\\Users\\Otomi\\Desktop\\Learning\\Programming\\Python\\Practice')
