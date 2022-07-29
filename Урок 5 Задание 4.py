# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('RLE1.txt', 'r') as data:
    my_text = data.read()

def coding(a):
    count = 1
    res = ''
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            count += 1
        else:
            res = res + str(count) + a[i]
            count = 1
    if count > 1 or (a[len(a)-2] != a[-1]):
        res = res + str(count) + a[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

print(my_text)
print(coding(my_text))
print(decoding(coding(my_text)))

with open('RLE2.txt', 'w') as data:
    my_text2 = data.write(decoding(coding(my_text)))
