import random

print('Введите количество элементов массива N:')
N = int(input())

list = [0] * N

for i in range(N):
		list[i] = random.randint(-N,N)
		
print(list)

print('Введите позицию a:')
a = int(input())
print('Введите позицию b:')
b = int(input())

prod = list[a - 1] * list[b - 1]
print('Произведение равно: ', prod)
