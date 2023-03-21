# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

MAX_WEIGHT = 15


def pack_backpack(things: dict) -> list:
    current_weight = 0
    backpack = []
    for item, weight in things.items():
        current_weight += weight
        if current_weight <= MAX_WEIGHT:
            backpack.append(item)
    return backpack


stuff = {
    "sleeping_bad": 1.5,
    "tent": 4,
    "dish": 1.5,
    "food": 5,
    "water": 5,
    "clothes": 2,
    "boat": 5
}

print(pack_backpack(stuff))
