from decimal import Decimal


class Terminal:
	MULTIPLICITY = 50
	TAX: Decimal = Decimal(0.015)
	BONUS: Decimal = Decimal(0.03)
	WEALTH_TAX: Decimal = Decimal(0.1)
	WEALTH: Decimal = Decimal(5e6)
	TAX_UPPER_LIMIT: Decimal = Decimal(600)
	TAX_LOWER_LIMIT: Decimal = Decimal(30)
	sum_account = 0
	operation_count = 0
	operations_log = []
	
	def __init__(self):
		print("Hello!")
	
	def enter_operation_sum(self):
		count = 0
		while count < 3:
			money = Decimal(input("Enter the amount of money to operation: "))
			if money % self.MULTIPLICITY == 0:
				return money
			else:
				print("You can enter the amount in multiples of 50")
				count -= 1
		else:
			print("You entered the wrong amount three times")
			return 0
	
	def get_wealth_tax(self):
		if self.sum_account > self.WEALTH:
			tax = self.sum_account * self.WEALTH_TAX
			self.sum_account -= tax
			print(f"Wealth tax = {round(tax, 2)}, your total sum = {round(self.sum_account, 2)}")
		return self.sum_account
	
	def refinancing(self, operation_sum):
		if self.operation_count % 3 == 0:
			bonus = operation_sum * self.BONUS
			self.sum_account += bonus
			print(f"Bonus = {round(bonus, 2)}, your total sum = {round(self.sum_account, 2)}")
	
	def top_up(self):
		sum_to_put: Decimal = self.enter_operation_sum()
		if sum_to_put > 0:
			self.sum_account = self.get_wealth_tax()
			self.sum_account += sum_to_put
			print(f"Account replenished with {round(sum_to_put, 2)}.\nTotal sum {round(self.sum_account, 2)}")
			self.operation_count += 1
			self.refinancing(sum_to_put)
			self.operations_log.append(("Replenishment", sum_to_put))
	
	def take_off(self):
		sum_to_take: Decimal = self.enter_operation_sum()
		self.sum_account = self.get_wealth_tax()
		if sum_to_take > self.sum_account:
			print("Insufficient funds in the account")
			return
		elif sum_to_take > 0:
			self.sum_account -= sum_to_take
			tax = sum_to_take * self.TAX
			if tax < 30:
				self.sum_account -= 30
				print("Tax = 30")
			elif tax > 600:
				self.sum_account -= 600
				print("Tax = 600")
			else:
				self.sum_account -= tax
				print(f"Tax = {round(tax, 2)}")
		print(f"Cash dispensed: {round(sum_to_take, 2)}.\nTotal sum {round(self.sum_account, 2)}")
		self.operation_count += 1
		self.refinancing(sum_to_take)
		self.operations_log.append(("Withdrawals", sum_to_take))
	
	def print_log(self):
		if len(self.operations_log) == 0:
			print("No cash transactions")
		else:
			for index, log in enumerate(self.operations_log, start=1):
				print(f"{index}. {log[0]}: {int(log[1])}")
	
	def exit_(self):
		print("Good bye!")
	
	def main(self):
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
					self.top_up()
				case 2:
					self.take_off()
				case 3:
					print(round(self.sum_account, 2))
				case 4:
					self.print_log()
				case 5:
					self.exit_()
					break
				case _:
					print("Internal error")


if __name__ == '__main__':
	a = Terminal()
	a.main()
