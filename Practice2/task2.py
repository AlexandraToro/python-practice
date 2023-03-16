# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction


# Вычисление суммы дробей
def get_sum_fractions(fr1: str, fr2: str) -> str:
    n1, d1 = split_fraction(fr1)
    n2, d2 = split_fraction(fr2)
    if d1 == d2:
        num = n1 + n2
        den = d1
    else:
        num = n1 * d2 + n2 * d1
        den = d1 * d2
    num, den = fraction_reduction(num, den)
    return f"{num}/{den}"


# вычисление произведения дробей
def get_prod_fractions(fr1: str, fr2: str) -> str:
    n1, d1 = split_fraction(fr1)
    n2, d2 = split_fraction(fr2)
    num = n1 * n2
    den = d1 * d2
    num, den = fraction_reduction(num, den)
    return f"{num}/{den}"


# сокращение дроби
def fraction_reduction(num1, num2):
    gcd = find_greatest_common_divisor(num1, num2)
    num1 /= gcd
    num2 /= gcd
    return int(num1), int(num2)


# поиск наибольшего общего делителя
def find_greatest_common_divisor(a, b: int):
    if a > b:
        min_ = b
    else:
        min_ = a
    for i in range(1, min_ + 1):
        if (a % i == 0) and (b % i == 0):
            gcd = i
    return gcd


# разделение строковой дроби на числитель и знаменатель
def split_fraction(fr: str):
    n, d = map(int, fr.split("/"))
    return n, d


def main():
    first = "13/75"
    second = "2/3"
    print(f" {first} + {second} = {get_sum_fractions(first, second)}")
    print(f" {first} * {second} = {get_prod_fractions(first, second)}")
    num1 = Fraction(13, 75)
    num2 = Fraction(2, 3)
    print(f" Review:\n"
          f" sum = {num1 + num2}, \n"
          f" prod = {num1 * num2}")


main()
