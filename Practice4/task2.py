# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение переданного
# аргумента, а значение - имя аргумента. Если ключ не хешируем, используйте его строковое представление.

from collections.abc import Hashable


def dict_of_kwargs(**kwargs):
    return {val if isinstance(val, Hashable) else str(val): key for key, val in kwargs.items()}


print(dict_of_kwargs(a=3, b="bjdhfvbd", c=[4, 5, 6, 6], d={1: "vnjkn", 2: "jkhbvd"}))
