# Задание №1

class CashRegister:
    def __init__(self, initial_amount=0):
        self.balance = initial_amount  # Начальный баланс кассы
    
    def top_up(self, amount):
        """Пополняет кассу на указанную сумму"""
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.balance += amount
    
    def count_1000(self):
        """Возвращает количество целых тысяч в кассе"""
        return self.balance // 1000
    
    def take_away(self, amount):
        """Забирает указанную сумму из кассы"""
        if amount <= 0:
            raise ValueError("Сумма изъятия должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно денег в кассе")
        self.balance -= amount

# Пример использования
kassa = CashRegister(5000)  # Создаем кассу с начальным балансом 5000

kassa.top_up(3000)  # Пополняем на 3000
print(f"Текущий баланс: {kassa.balance}")
print(f"Целых тысяч: {kassa.count_1000()}")

kassa.take_away(2000)  # Забираем 2000
print(f"Текущий баланс: {kassa.balance}")
print(f"Целых тысяч: {kassa.count_1000()}")

try:
    kassa.take_away(10000)  # Пытаемся забрать больше, чем есть
except ValueError as e:
    print(f"Ошибка: {e}")

# Задание №2

class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s
    
    def go_up(self):
        self.y += self.s
    
    def go_down(self):
        self.y -= self.s
    
    def go_left(self):
        self.x -= self.s
    
    def go_right(self):
        self.x += self.s
    
    def evolve(self):
        self.s += 1
    
    def degrade(self):
        if self.s <= 1:
            raise ValueError("Шаг не может быть меньше или равен 0")
        self.s -= 1
    
    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        steps_x = (dx + self.s - 1) // self.s
        steps_y = (dy + self.s - 1) // self.s
        return steps_x + steps_y

t = Turtle(0, 0, 2)

t.go_up()
t.go_right()
print(f"Позиция: ({t.x}, {t.y})")

t.evolve()
t.go_left()
print(f"Позиция: ({t.x}, {t.y})")

try:
    t.degrade()
    t.degrade()
    t.degrade()
except ValueError as e:
    print(f"Ошибка: {e}")

moves = t.count_moves(10, 10)
print(f"Минимальное количество ходов до (10, 10): {moves}")