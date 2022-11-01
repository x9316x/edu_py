print('Введите число n:')
n = int(input())

sub = [0] * n
sum = 0
for i in range(n):
		sub[i] = (1 + 1 / (i + 1) )**(i + 1)
		sum = sum + sub[i]

print(round(sum,3))
