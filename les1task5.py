from math import sqrt

print('Введите значение x точи A:')
Ax = float(input())
print('Введите значение y точи A:')
Ay = float(input())
print('Введите значение x точи B:')
Bx = float(input())
print('Введите значение y точи B:')
By = float(input())

print('Расстояние между точками A и B = ')
AB = sqrt(((Bx - Ax)**2) + ((By - Bx)**2))

print(AB)
