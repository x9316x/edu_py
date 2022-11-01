print('Введите номер дня недели:')
day = int(input())
while(day < 1) or (day > 7):
	print('В неделе 7 дней, введите число от 1 до 7!')
	day = int(input())

if (day == 7) or (day == 6):
	print(day, 'день - выходной')
else:
	print(day, ' день - будний')
