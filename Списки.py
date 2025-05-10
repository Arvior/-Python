# Задание №1

N = int(input())
numbers = [int(input()) for i in range(N)]
for num in reversed(numbers):
    print(num)

# Задание №2

n = int(input())
arr = list(map(int, input().split()))
last = arr.pop()
arr.insert(0, last)
print(' '.join(map(str, arr)))

# Задание №3

m = int(input())  # Максимальная нагрузка лодки
n = int(input())  # Количество рыбаков
weights = [int(input()) for i in range(n)]  
weights.sort()  

left = 0
right = n - 1
boats = 0

while left <= right:
    if weights[left] + weights[right] <= m:
        left += 1  
    right -= 1  
    boats += 1

print(boats)