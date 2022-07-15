# Реализуйте алгоритм перемешивания списка.

import random

my_list = [1, 2, 3, 4, 5, 6]


def shuffled_list(my_list):
    print('Начальный список:    ' + str(my_list))

    for i in range(len(my_list)-1, 0, -1):

        j = random.randint(0, i+1)

        my_list[i], my_list[j] = my_list[j], my_list[i]

    print('Перемешанный список:   ' + str(my_list))


shuffled_list(my_list)
