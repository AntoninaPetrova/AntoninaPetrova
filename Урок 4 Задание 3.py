# Задайте последовательность чисел. Напишите программу, которая выведет список
#  неповторяющихся элементов исходной последовательности.

from random import randint

def create_list(size, a, b):
    return [randint(a, b) for i in range(size)]

def findUnic(list):
    return [i for i in set(my_list)]

size = int(input('Введите количество элементов последовательности '))
a = 1
b = 10

my_list = create_list(size, a, b)
print(my_list)
print(findUnic(my_list))