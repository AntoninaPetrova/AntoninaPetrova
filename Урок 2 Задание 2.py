# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел
# от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def searchNumber(a, n):
    a = 1
    my_list = [1]
    i = 1
    while len(my_list) < n:
        my_list.append(my_list[i-1]*(i+1))
        i += 1
    return my_list


n = int(input('Введите число N:   '))
print(f"Набор произведений чисел от 1 до {n}:   {searchNumber(1, n)}")