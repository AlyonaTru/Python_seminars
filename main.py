
# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
#
# if num1 == num2**2 or num2 == num1**2:
#     print('да')
#
# else:
#     print('нет')

# num1, num2, num3, num4, num5 = map(int, input().split(', '))
#  if num1 > num2, num3, num4, num5
#      print(f'максимальное число = {num1}')

# numbers = []
# for _ in range(5):
#     n = int(input())
#     numbers.append(n)
#
# maxx = numbers[0]
# for el in numbers:
#     if el > maxx:
#         maxx = el
#
# print(maxx)
#
# num = float(input())
# if num%1 !=0:
#     num = num*10
#     num = int(num)
#     num = num%10
#     print(num)
# else:
#     print('нет')

#5.
num = int(input())

if (num % 5 ==0 and num%10 ==0 or num% 15 ==0) and num%30 ==1:
    print('да')
else:
    print('нет')