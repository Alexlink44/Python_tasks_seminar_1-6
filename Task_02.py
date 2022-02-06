# Найти максимальное из пяти чисел

lst = ['a', 'b', 'c', 'd', 'e']

numbers = []
# for i in lst:
#     print(f'Введита число {i}')
#     numbers.append(float(input()))

i = 0
while len(lst) != i:
    print(f'Введита число {lst[i]}')
    numbers.append(float(input()))
    i += 1
max = numbers[0]

def f(x, max):
    if x == len(numbers):
        return max
    elif max < numbers[x]:
        max = numbers[x]
        x += 1
        return f(x, max)
    else:
        x += 1
        return f(x, max)

max = f(0, max)
print(max)