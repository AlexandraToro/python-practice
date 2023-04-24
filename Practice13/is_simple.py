# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

#пример со встроенным исключением и его обработкой


def is_simple():
	while True:
		try:
			num = int(input("Enter integer between 1 and 100 000: "))
			break
		except ValueError as e:
			print('Received an invalid value.\n'
			      'You must enter a numeric value, for example: 2 or 45')
	flag = True
	if 1 <= num <= 100000:
		for n in range(2, num - 1):
			if num % n == 0:
				print(f"Number {num} is composite.")
				flag = False
				break
		if flag:
			print(f"Number {num} is simple.")
	else:
		print("Invalid number. Please, repeat.")


if __name__ == '__main__':
	is_simple()
	