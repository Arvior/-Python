# Задание №1

s = input("Введите строку: ")
if s == s[::-1]:
    print("yes")
else:
    print("no")

# Задание №2

s = input("Введите строку: ")
a = ' '.join(s.split())
print(a)