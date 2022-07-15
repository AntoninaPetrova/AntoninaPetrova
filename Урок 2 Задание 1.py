# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input("Введите вещественное число: ")


def charSum(num):
    sum = 0
    for a in str(num):
        if a == "." or a == "," or a == "-":
            continue
        sum += int(a)
    return sum


print(f"Сумма цифр равна:  {charSum(number)}")