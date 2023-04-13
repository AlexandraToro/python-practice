_log_ = {}


def guess(text: str, answer: list[str], count: int) -> int:
	for i in range(count):
		answer_user = input(f"{text}: ").lower()
		if answer_user in answer:
			print("U win!")
			log(text, i + 1)
			print_log()
			return i + 1
	log(text, 0)
	print_log()
	return 0


def log(text: str, count: int) -> None:
	_log_ = {text: count}


def print_log() -> None:
	for question, answer in _log_.items():
		print(f"Загадка: '{question}' была отгадана за {answer} попытки")


if __name__ == '__main__':
	a = guess("Зимой и летом одним цветом", ["ель", "ёлка", "елка"], 3)
