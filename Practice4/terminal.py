# Разбейте её на отдельные операции - функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег


from decimal import Decimal

MULTIPLICITY = 50
TAX: Decimal = Decimal(0.015)
BONUS: Decimal = Decimal(0.03)
WEALTH_TAX: Decimal = Decimal(0.1)
WEALTH: Decimal = Decimal(5e6)
TAX_UPPER_LIMIT: Decimal = Decimal(600)
TAX_LOWER_LIMIT: Decimal = Decimal(30)
sum_account: Decimal = Decimal(0)
operation_count = 0
operations_log = []


def enter_operation_sum():
	count = 0
	while count < 3:
		money = Decimal(input("Enter the amount of money to operation: "))
		if money % MULTIPLICITY == 0:
			return money
		else:
			print("You can enter the amount in multiples of 50")
			count -= 1
	else:
		print("You entered the wrong amount three times")
		return 0


def get_wealth_tax():
	global sum_account
	if sum_account > WEALTH:
		tax = sum_account * WEALTH_TAX
		sum_account -= tax
		print(f"Wealth tax = {round(tax, 2)}, your total sum = {round(sum_account, 2)}")
	return sum_account


def refinancing(operation_sum):
	global sum_account
	if operation_count % 3 == 0:
		bonus = operation_sum * BONUS
		sum_account += bonus
		print(f"Bonus = {round(bonus,2)}, your total sum = {round(sum_account,2)}")


def top_up():
	global operation_count
	global sum_account
	sum_to_put: Decimal = enter_operation_sum()
	if sum_to_put > 0:
		sum_account = get_wealth_tax()
		sum_account += sum_to_put
		print(f"Account replenished with {round(sum_to_put, 2)}.\nTotal sum {round(sum_account, 2)}")
		operation_count += 1
		refinancing(sum_to_put)
		operations_log.append(("Replenishment", sum_to_put))


def take_off():
	global operation_count
	global sum_account
	sum_to_take: Decimal = enter_operation_sum()
	sum_account = get_wealth_tax()
	if sum_to_take > sum_account:
		print("Insufficient funds in the account")
		return
	elif sum_to_take > 0:
		sum_account -= sum_to_take
		tax = sum_to_take * TAX
		if tax < 30:
			sum_account -= 30
			print("Tax = 30")
		elif tax > 600:
			sum_account -= 600
			print("Tax = 600")
		else:
			sum_account -= tax
			print(f"Tax = {round(tax, 2)}")
	print(f"Cash dispensed: {round(sum_to_take, 2)}.\nTotal sum {round(sum_account, 2)}")
	operation_count += 1
	refinancing(sum_to_take)
	operations_log.append(("Withdrawals", sum_to_take))


def print_log():
	if len(operations_log) == 0:
		print("No cash transactions")
	else:
		for index, log in enumerate(operations_log, start=1):
			print(f"{index}. {log[0]}: {int(log[1])}")


def exit_():
	print("Good bye!")


def main():
	while True:
		menu = int(input("Menu: \n"
		                 "1: Replenishment\n"
		                 "2: Withdraw cash\n"
		                 "3: Show total sum\n"
		                 "4: Show operation's history\n"
		                 "5: Exit\n"
		                 "Print number of needed operation: "))
		match menu:
			case 1:
				top_up()
			case 2:
				take_off()
			case 3:
				print(round(sum_account,2))
			case 4:
				print_log()
			case 5:
				exit_()
				break
			case _:
				print("Internal error")


main()
