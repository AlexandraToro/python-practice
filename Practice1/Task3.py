# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.

from random import randint
print("You need to guess an integer between 0 and 1000. You have 10 attempts. ")
num = randint(0, 1000)
count = 10
while count > 0:
    entered_num = int(input("Enter your integer: "))
    if 0 <= entered_num <= 1000:
        count -= 1
        if entered_num == num:
            print("You guessed it!")
            break
        elif entered_num > num:
            print("Your number is higher.")
        else:
            print("Your number is less.")
        print(f"Remaining attempts: {count}")
    else:
        print("Your integer not included in the given interval (0-1000).")
        continue
else:
    print("No more attempts. Game over.")
