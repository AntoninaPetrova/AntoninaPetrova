# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_str = 'Привет, мойабв Мир! Я очень приабвочень люблю, когда программа абвПайтон работает'
res = [word for word in my_str.split() if 'абв' not in word]
# print(res)  выведет ['Привет,', 'Мир!', 'Я', 'очень', 'люблю,', 'когда', 'пргограмма', 'работает']

print(' '.join(res))