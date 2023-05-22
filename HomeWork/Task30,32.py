import random
"""
Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и
количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии:
an = a1 + (n-1) * d
Каждое число вводится с новой строки.
Ввод:             Вывод:
7 2 5             7 9 11 13 15
"""
def task_30():
  first_Number = int(input("Enter the first number of the list, please: "))
  difference_Number = int(input("Enter the difference between the elements, please: "))
  size_List = int(input("Enter the size of the list, please: "))
  use_List = [(first_Number + i*difference_Number) for i in range(size_List)]
  print (*use_List)

"""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)
Индекс:   0  1  2  3   4   5  6  7   8   9 10 11  12 13  14  15 16  17  18 19
Ввод:   [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]                       
Вывод:  [1, 9, 13, 14, 19]
"""
def task_32():
  size_List = int(input("Enter the size of the list, please: "))
  use_List = [random.randint(-40,40) for i in range(size_List)]
  print (*use_List)
  min_Number = int(input("Enter the minium number of the list, please: "))
  max_Number = int(input("Enter the maximum number of the list, please: "))
  range_List = [i for i in range(len(use_List)) if  min_Number <= use_List[i] <= max_Number]
  print (*range_List)


task_30()
task_32()