# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def get_path(abs_path: str) -> tuple[str, str, str]:
	a, extension = abs_path.rsplit('.', 1)
	file_path, file_name = a.rsplit('\\', 1)
	return file_path, file_name, extension


text = "C:\\Users\\Otomi\\Desktop\\Learning\\QA\\web1\\Hw2\\project.html"
print(get_path(text))
