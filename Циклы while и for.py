# Задание №1

N = int(input("Введите количество чисел: "))
count_zero = 0

for i in range(N):
    num = int(input("Введите число: "))
    if num == 0:
        count_zero += 1

print(f"Количество нулей: {count_zero}")

# Задание №2

X = int(input("Введите натуральное число X: "))
count = 0
sqrt_X = int(X ** 0.5) + 1

for i in range(1, sqrt_X):
    if X % i == 0:
        if i * i == X:
            count += 1
        else:
            count += 2

print(f"Количество натуральных делителей: {count}")

# Задание №3

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

even_numbers = [str(x) for x in range(A, B + 1) if x % 2 == 0]

print(' '.join(even_numbers))