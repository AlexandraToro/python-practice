# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


def to_convert_hex(num: int) -> str:
    result = ""
    while num != 0:
        match (num % 16):
            case 10: res = "a"
            case 11: res = "b"
            case 12: res = "c"
            case 13: res = "d"
            case 14: res = "e"
            case 15: res = "f"
            case _: res = str(num % 16)
        result = res + result
        num //= 16
    return result


print(to_convert_hex(555), hex(555))
print(to_convert_hex(888), hex(888))
print(to_convert_hex(123134), hex(123134))


