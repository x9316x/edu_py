import random
print('Введите количество элементов массива N:')
N = int(input())

list = [0] * N
sum = 0

for i in range(N):
		list[i] = random.randint(0, 9)
		
print(list)

for i in range(N):
	if i % 2 != 0:
		sum = sum + list[i]

print(sum)
