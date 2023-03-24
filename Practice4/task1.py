# Напишите функцию для транспонирования матрицы

def matrix_transposition(matrix_: list[list[int]]) -> list[list[int]]:
    new_matrix = []
    for i in range(len(matrix_[0])):
        new_matrix.append([])
        for j in range(len(matrix_)):
            new_matrix[i].append(matrix_[j][i])
    return new_matrix


def print_matrix(matrix: list[list[int]]):
    for xy in matrix:
        print(xy)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix(matrix)
print()
print_matrix(matrix_transposition(matrix))
