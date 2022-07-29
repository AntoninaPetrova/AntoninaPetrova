# Игра в конфеты. Человек против бота (у меня Чебурашка):

from random import randint

def input_candy(name):
    x = int(input(f"{name}, введите количество конфет от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. На столе осталось {value} конфет.")

player1 = input("Введите Ваше имя: ")
player2 = 'Чебурашка' # так зовут моего бота)
value = 2021
flag = randint(0,2) 
if flag:
    print(f"Первый ходит {player1}")
else:
    print('Первый ходит Чебурашка')

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_candy(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = randint(1,28) 
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Поздравляем! Выиграл {player1}!")
else:
    print(f"Выиграл Чебурашка, а вам повезет в следующий раз!")