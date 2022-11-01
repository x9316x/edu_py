import random
print('Введите количество элементов массива N:')
N = int(input())

list = [0] * N

if N % 2 == 0:
	arr = [0] * int((N / 2))
else:
	arr = [0] * int(((N + 1) / 2))

for i in range(N):
		list[i] = random.randint(0, 9)
		
print(list)

first = 0
last = N - 1
k = 0 

for i in range(N):
	if k < (N / 2):
		arr[i] = list[first] * list[last]
		first = first + 1
		last = last - 1
	k = k + 1

print(arr)
