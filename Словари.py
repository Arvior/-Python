# Задание №1

pets = {}

def get_age_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return 'год'
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return 'года'
    else:
        return 'лет'

pet_name = input("Введите кличку питомца: ")
pets[pet_name] = {
    'Вид питомца': input("Введите вид питомца: "),
    'Возраст питомца': int(input("Введите возраст питомца: ")),
    'Имя владельца': input("Введите имя владельца: ")
}

pet_data = pets[pet_name]
age = pet_data['Возраст питомца']
age_suffix = get_age_suffix(age)

info = (
    f'Это {pet_data["Вид питомца"].lower()} по кличке "{pet_name}". '
    f'Возраст питомца: {age} {age_suffix}. '
    f'Имя владельца: {pet_data["Имя владельца"]}'
)
print(info)

# Задание №2

my_dict = {}

for num in range(10, -6, -1):
    my_dict[num] = num ** num

print(my_dict)