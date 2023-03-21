# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


def get_duplicate_elements(input_list: list) -> list:
    new_set = set()
    for i in input_list:
        if input_list.count(i) > 1:
            new_set.add(i)
    return list(new_set)


first_list = [1, 3, 2, 4, 5, 5, 6, 6, 7, 8, 1, 6, 5, 3, 6, 12, 6, 12]
print(get_duplicate_elements(first_list))
second_list = ["мама", "папа", "бабушка", "мама", "дедушка", "папа", "сестра"]
print(get_duplicate_elements(second_list))

