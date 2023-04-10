# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне  [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на
# проверку.

from sys import argv

__all__ = ['check_date']


def check_date(date: str) -> bool:
	d, m, y = map(int, date.split("."))
	if y > 9999 or y < 1 or m > 12 or d > 31:
		return False
	elif (m in [4, 6, 9, 11]) and d > 30:
		return False
	elif m == 2 and _is_leap(y) and d > 29:
		return False
	elif m == 2 and not _is_leap(y) and d > 28:
		return False
	else:
		return True


def _is_leap(year):
	if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
		return True
	else:
		return False


if __name__ == "__main__":
	name, *arg = argv
	print(check_date(*arg))
