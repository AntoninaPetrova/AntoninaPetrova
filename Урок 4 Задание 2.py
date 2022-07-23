# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def multipliers(n):
    i = 2
    my_list = []
    while i * i <= n:
        while n % i == 0:
            my_list.append(i)
            n = n / i
        i += 1
    if n > 1:
        my_list.append(n)
    return my_list


n = int(input('Введите натуральное число N '))
print(multipliers(n))
