# Задание №1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def factorial_sequence(start_num):
    initial_fact = factorial(start_num)

    result = []
    for num in range(initial_fact, 0, -1):
        result.append(factorial(num))
    
    return result

number = 3
result_sequence = factorial_sequence(number)
print(f"Факториал числа {number}: {factorial(number)}")
print(f"Результирующий список: {result_sequence}")

# Задание №2

import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return 'год'
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return 'года'
    else:
        return 'лет'

def get_pet(ID):
    return pets[ID] if ID in pets else False

def pets_list():
    for ID, pet_info in pets.items():
        for name, data in pet_info.items():
            age = data['Возраст питомца']
            print(f"ID: {ID} | Кличка: {name} | Вид: {data['Вид питомца']} | "
                  f"Возраст: {age} {get_suffix(age)} | Владелец: {data['Имя владельца']}")

def create():
    last = collections.deque(pets, maxlen=1)[0] if pets else 0
    new_id = last + 1
    
    name = input("Введите кличку питомца: ")
    pet_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")
    
    pets[new_id] = {
        name: {
            "Вид питомца": pet_type,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print(f"Добавлен новый питомец с ID {new_id}")

def read(ID):
    pet_info = get_pet(ID)
    if not pet_info:
        print(f"Питомец с ID {ID} не найден")
        return
    
    name = list(pet_info.keys())[0]
    data = pet_info[name]
    age = data['Возраст питомца']
    
    print(f'Это {data["Вид питомца"]} по кличке "{name}". '
          f'Возраст питомца: {age} {get_suffix(age)}. '
          f'Имя владельца: {data["Имя владельца"]}')

def update(ID):
    pet_info = get_pet(ID)
    if not pet_info:
        print(f"Питомец с ID {ID} не найден")
        return
    
    name = list(pet_info.keys())[0]
    print(f"Текущая информация о питомце:")
    read(ID)
    
    print("\nВведите новые данные (оставьте поле пустым, чтобы не изменять):")
    new_name = input(f"Кличка [{name}]: ") or name
    pet_type = input(f"Вид [{pet_info[name]['Вид питомца']}]: ") or pet_info[name]['Вид питомца']
    age = input(f"Возраст [{pet_info[name]['Возраст питомца']}]: ") or pet_info[name]['Возраст питомца']
    owner = input(f"Владелец [{pet_info[name]['Имя владельца']}]: ") or pet_info[name]['Имя владельца']
    
    del pets[ID]
    pets[ID] = {
        new_name: {
            "Вид питомца": pet_type,
            "Возраст питомца": int(age),
            "Имя владельца": owner
        }
    }
    print("Информация обновлена!")

def delete(ID):
    if ID in pets:
        del pets[ID]
        print(f"Питомец с ID {ID} удален")
    else:
        print(f"Питомец с ID {ID} не найден")

while True:
    print("\nДоступные команды: create, read, update, delete, list, stop")
    command = input("Введите команду: ").lower()
    
    if command == 'stop':
        break
    elif command == 'create':
        create()
    elif command == 'read':
        ID = int(input("Введите ID питомца: "))
        read(ID)
    elif command == 'update':
        ID = int(input("Введите ID питомца: "))
        update(ID)
    elif command == 'delete':
        ID = int(input("Введите ID питомца: "))
        delete(ID)
    elif command == 'list':
        pets_list()
    else:
        print("Неизвестная команда")