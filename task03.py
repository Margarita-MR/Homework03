# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, 
# отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from fractions import Fraction
import math
import decimal
from decimal import Decimal

n = int(input('Количество вещественных чисел = '))
import random
x=list(round(random.uniform(0, 10), 2) for x in range(n))

print(x)
x = str(x)

x=(x.replace('.',', '))

# print(type(x))
x = x.split(',')
print(x)
# print(type(x))

A = list(x[1:len(x):2])
print(A)


Max = max(A)
print('Максимальное значение дробной части : ', Max)
Min = min(A)
print('Минимальное значение дробной части : ', Min)
print('Разность = ', int(Max)-int(Min))



