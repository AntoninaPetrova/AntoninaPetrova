# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def get_fibonacci(k):
    fibo_nums = []
    a, b = 1, 1
    for i in range(k):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(k+1):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums


k = int(input('Введите число: '))
print(get_fibonacci(k))
