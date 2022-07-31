# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def find_diff(my_list):

    nums = [round(i - int(i), 10) for i in (my_list)] # List Comprehension 
    print('Максимальное значение дробной части элементов: ', max(nums))
    print('Минимальное значение дробной части элементов: ', min(nums))

    return max(nums) - min(nums)


my_list = [1.1, 1.2, 3.1, 5, 10.01]

print('Разница между MAX и MIN значением дробной части элементов: ', find_diff(my_list))
