print('Введите переменную x отличную от нуля:')
x = int(input())
while(x == 0):
	print('Введите переменную x отличную от нуля!')
	x = int(input())

print('Введите переменную y отличную от нуля:')		
y = int(input())
while(y == 0):
	print('Введите переменную x отличную от нуля!')
	y = int(input())
	

if (x > 0) and (y > 0):
	print('Первая четверть')
elif (x > 0) and (y < 0):
	print('Четвертая четверть')
elif (x < 0) and (y > 0):
	print('Вторая четверть')
else:
	print('Третья четверть')
