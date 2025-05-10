# Задание №1

num = int(input("Введите целое число: "))

if num == 0:
    print("нулевое число")
else:
    if num > 0:
        sign = "положительное"
    else:
        sign = "отрицательное"

    if num % 2 == 0:
        parity = "четное"
        print(f"{sign} {parity} число")
    else:
        parity = "нечетное"
        print(f"{sign} {parity} число")
        print("число не является четным")

# Задание №2

word = input("Введите слово из маленьких латинских букв: ").lower()

glasnie = {'a', 'e', 'i', 'o', 'u'}
glasnie_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
total_glasnie = 0
total_consonants = 0

for letter in word:
    if letter in glasnie:
        total_glasnie += 1
        glasnie_counts[letter] += 1
    elif letter.isalpha():
        total_consonants += 1

print(f"Общее количество гласных: {total_glasnie}")
print(f"Общее количество согласных: {total_consonants}")

# Выводим количество каждой гласной или False, если её нет
for glasnie in sorted(glasnie_counts):
    count = glasnie_counts[glasnie]
    print(f"{glasnie}: {count if count > 0 else False}")

# Задание №3

X = int(input("Введите минимальную сумму инвестиций: "))
A = int(input("Сколько долларов у Майкла? "))
B = int(input("Сколько долларов у Ивана? "))

if A >= X and B >= X:
    print("Да вы оба можете инвестировать")
elif A >= X:
    print("Только Майкл")
elif B >= X:
    print("Только Иван")
elif A + B >= X:
    print("Ну если вместе то окей")
else:
    print("Сорян денег нехватает")