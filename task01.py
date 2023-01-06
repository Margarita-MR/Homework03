# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import operator
import math
from random import randrange
from xml.etree import ElementInclude
n = int(input('Введите максимальное число = '))
i = int(input('Введите количество чисел = '))
a = list(randrange(1, n) for i in range(i))
print('Список чисел : ', a)

A = list(a[1:i:2])
print('Числа с нечетными индексами : ', A)
S = sum(A)
print('Сумма чисел = ', S)




# import operator
# import math
# from random import randrange
# from xml.etree import ElementInclude
# n = int(input('Введите максимальное число = '))
# i = int(input('Введите количество чисел = '))
# a = list(randrange(1, n) for i in range(i))
# print(a)

# A = list(a[1:i:2])
# print(A)
# B = list(reversed(A))
# # print(B)

# Mul = list(map(operator.mul, A, B))
# print(Mul)

# middle = float(len(Mul))/2
# if middle % 2 != 0:
#     x = int(Mul[int(middle - .5)])
# else:
#     x = int(Mul[int(middle)], Mul[int(middle-1)])
# # print(x)
# k = Mul.index (x)
# Res = list(Mul[0:k+1:1])
# print(Res)