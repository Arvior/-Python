# Задание №1

try:
    a = float(input("Введите длину первой стороны прямоугольника: "))
    b = float(input("Введите длину второй стороны прямоугольника: "))
    
    if a <= 0 or b <= 0:
        print("Ошибка: стороны должны быть положительными числами")
    else:
        area = a * b
        perimeter = 2 * (a + b)

        print(f"Площадь прямоугольника: {round(area, 2)}")
        print(f"Периметр прямоугольника: {round(perimeter, 2)}")
        
except ValueError:
    print("Ошибка: введены некорректные данные. Пожалуйста, введите числа.")

# Задание №2

number = int(input("Введите пятизначное число: "))

tens_of_thousands = number // 10000  # десятки тысяч
thousands = (number // 1000) % 10     # тысячи
hundreds = (number // 100) % 10       # сотни
tens = (number // 10) % 10            # десятки
units = number % 10                   # единицы

step1 = tens ** units                # десятки в степени единиц
step2 = step1 * hundreds             # умножаем на сотни
step3 = tens_of_thousands - thousands  # разность дес.тыс. и тыс.
result = step2 / step3               # делим на разность

print(f"Результат: {result}")
