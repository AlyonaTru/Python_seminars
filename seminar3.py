#задачка на перемешивание списка
# import time
#
# def random_without_lib(x):
#     time.sleep(0.001)
#     return int(round(time.time() * 1000) % x)
# lst = [random_without_lib(10) for i in range(10)]
#
# print(lst)
#
# for i in range(len(lst)):
#     lst[i], lst[random_without_lib(len(lst))] = lst[random_without_lib(len(lst))], lst[i]
#
# print(lst)

#Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# lst = ['blue', 'r3d','gre2n', 'hello']
# f = False
# for i in range(len(lst)):
#     if '2' in lst[i]:
#         f = True
#         break
# print(f)

#3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

lst = ["йцу","фыв","ячс","цук","йцукен","йцу"]
lst2 = "йцу"
count = 0
res = -1
for i in range(len(lst)):
    if lst[i] == lst2:
        count += 1
    if count == 2:
        res = i
    break
print(res)

#1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# lst = [2, 10, 10, 9, 3]
# summ = 0
# for i in range(len(lst)):
#     if i%2 !=0:
#         summ = summ+lst[i]
#
# print(summ)
