# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import operator
import math
from random import randrange
from xml.etree import ElementInclude
n = int(input('Введите максимальное число = '))
i = int(input('Введите количество чисел = '))
A = list(randrange(1, n) for i in range(i))
print(f'Список чисел : ', A)

B = list(reversed(A))
# print(B)

Mul = list(map(operator.mul, A, B))
# print(Mul)

middle = float(len(Mul))/2
if middle % 2 != 0:
    x = int(Mul[int(middle - .5)])
else:
    x = int(Mul[int(middle)])
# print(x)
k = Mul.index (x)
Res = list(Mul[0:k+1:1])
print(f'Произведение пар чисел : ', Res)
