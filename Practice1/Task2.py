# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


num = int(input("Enter integer between 1 and 100 000: "))
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
