import random
print('Введите количество элементов массива N:')
N = int(input())

list = [0] * N
temp = 0

for i in range(N):
		list[i] = random.randint(-N, N)
		
print(list)

for i in range(N):
	temp = list[i]
	tempIndex = random.randint(0, N-1)
	list[i] = list[tempIndex]
	list[tempIndex] = temp
	
print(list)
