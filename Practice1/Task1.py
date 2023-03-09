# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
# двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими
# сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = int(input("Enter first side of a triangle: "))
b = int(input("Enter second side of a triangle: "))
c = int(input("Enter third side of a triangle: "))

if a + b > c and b + c > a and a + c > b:
    print(f"The triangle is", end=" ")
    if a != b and b != c and c != b:
        print("scalene.")
    elif a == b and b == c:
        print("equilateral.")
    else:
        print("isosceles.")
else:
    print("Triangle with entered sides cannot exist.")
