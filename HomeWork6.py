
# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов 
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# a1 = int(input())
# n = int(input())
# d = int(input())

# count = 1
# while count <= n:
#     a = a1 + (count-1)*d
#     print(a, end = " ")
#     count +=1


# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
# lst_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9,  0, -5, -5, 7]
# mn = int(input("введите мин границу " ))
# mx = int(input('Введите максимальную границу '))
# lst_2 = []
# for i in range(len(lst_1)):
#     if  mn <= lst_1[i] <= mx:
#         lst_2.append(i)
# print(lst_2)