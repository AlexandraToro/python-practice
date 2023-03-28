# Создайте функцию генератор чисел Фибоначчи (см. Википедию)


def get_fibonacci(n):
	prev_fib = 0
	next_fib = 1
	for i in range(n):
		yield prev_fib
		next_fib = next_fib+prev_fib
		prev_fib = next_fib - prev_fib


fib = (get_fibonacci(10))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

