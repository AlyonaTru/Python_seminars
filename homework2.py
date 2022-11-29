# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#     *Пример:*
#     - 6782 -> 23
#     - 0.56 -> 11

# num = str(input('введите число '))
# summ = 0
# for i in num:
#     if i != '.':
#         summ = summ + int(i)
# print(summ)

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#     *Пример:*
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# num = int(input('введите число '))
# mult = 1
# for i in range(num):
#     i = i+1
#     mult = mult * i
#     print(mult, end = ' ')

# 3. Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.
#     *Пример:*
#     - Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37}
#     Необходимо сложить все значения словаря и вывести  сумму на экран.

# num = int(input('введите число '))
# dct = {}
# summ = 0
# for i in range (1, num+1):
#     dct[i] = (1 + 1/i)**i
#     summ = summ + dct[i]
#
# print(dct)
# print(round(summ, 2))

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import Random, randint

num = int(input('Введите число N: '))
numbers = []
for i in range(num):
    numbers.append(randint(-num, num + 1))

print(numbers)

f = open('file.txt', 'w')
while True:
    s = input('Укажите индекс умножаемого элемента - ')
    if s == "":
        break
    f.write(s + "\n")
f.close()

result = 1
f = open('file.txt', 'r')
for line in f:
    if line == "":
        break
    result *= numbers[int(line)]
f.close()
print(result)