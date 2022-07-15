# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.


def numberProduct(n, prod=0):
    prod += ((1 + 1 / n) ** n)
    return prod


n = int(input('Введите число N  '))
num = range(n)
numTotal = ' '
sumNum = 0
for i in range(1, n + 1):
    sumNum += numberProduct(i)
    numTotal += ' ' + str(numberProduct(i))
print(f'Сумма последовательности из {n} чисел = {sumNum}')
