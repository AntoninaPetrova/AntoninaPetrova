# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = input("Введите вещественное число: ")


def charSum(num):
    x = num.split(".")
    a = int(x[0])
    b = int(x[1])
    sum = 0
    while (a > 0):
        sum += a % 10
        a = a // 10
    while (b > 0):
        sum += b % 10
        b = b // 10
    return sum


print(f"Сумма цифр равна:  {charSum(num)}")
