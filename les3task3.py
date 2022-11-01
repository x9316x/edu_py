import random
print('Введите количество элементов массива N:')
N = int(input())

list = [0] * N
sum = 0

for i in range(N):
		list[i] = round(random.uniform(0, 9), 2)
		
print(list)

min = list[0] % 1
max = list[0] % 1

for i in range(1, N):
	if (list[i] % 1) < min:
		min = (list[i] % 1)
	elif (list[i] % 1) > max:
		max = (list[i] % 1)

print('Минимальная дробная часть - ', round(min, 2))
print('Максимальная дробная часть - ', round(max, 2))

res = max - min
print('Разница - ', round(res, 2))
