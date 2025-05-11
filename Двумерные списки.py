# Задание №1

import random

def create_and_add_matrices():
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    
    matrix_a = [[random.randint(-100, 100) for _ in range(cols)] for _ in range(rows)]
    matrix_b = [[random.randint(-100, 100) for _ in range(cols)] for _ in range(rows)]
    
    result = [[matrix_a[i][j] + matrix_b[i][j] for j in range(cols)] for i in range(rows)]
    
    print("\nМатрица A:")
    for row in matrix_a:
        print(row)
    
    print("\nМатрица B:")
    for row in matrix_b:
        print(row)
    
    print("\nРезультат сложения A + B:")
    for row in result:
        print(row)

create_and_add_matrices()