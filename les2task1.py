print('Введите число:')
num = input()
length = len(num)
sum = 0

for i in range(length):
	if num[i] != '.':
		sum = sum + int(num[i])
		
print('Сумма чисел данного числа равно = ',sum)
