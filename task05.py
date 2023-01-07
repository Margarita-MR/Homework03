# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи



import math
k = int(input('Введите количество чисел = '))
print(k)
index = []
for i in range(-k, k+1):
    index.append(i)
print(*index, sep=', ')
# print(type(index))

def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  elif n >= 2:
    return fib(n-1)+fib(n-2)
  else: 
    return fib(n+2)-fib(n+1)
numfib = []
for e in index:
  numfib.append(fib(e))
print(*numfib, sep=", ")