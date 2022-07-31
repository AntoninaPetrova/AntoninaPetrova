# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.

from random import randint


def getNumbers(n):
    return [randint(-n, n) for i in range(n)] # List Comprehension 


# def getProd(a, b):
#     prod = my_list[a]*my_list[b]
#     return prod

prod = lambda a, b: my_list[a]*my_list[b] #lamdda

n = int(input('Введите число N  '))
my_list = getNumbers(n)
print(f'Список из {n} элементов:   {my_list}')
a = int(input('Введите индекс первого множителя  '))
b = int(input('Введите индекс второго множителя  '))
print(f'Произведение элементов с индексами {a} и {b}:   {prod(a, b)}')


