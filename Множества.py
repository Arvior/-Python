# Задание №1

n = int(input())
numbers = list(map(int, input().split()))
a = []
for num in numbers:
    if num not in a:
        a.append(num)
print(len(a))

# Задание №2

n = int(input())
list1 = {int(input()) for _ in range(n)}

m = int(input())
list2 = {int(input()) for _ in range(m)}

print(len(list1 & list2))

# Задание №3

numbers = list(map(int, input().split()))
seen = set()

for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)