# from functools import reduce

# field = range (1, 10)

# def draw_field(field):
#     print('-------------')
#     for i in range(3):
#         print('|', field[0+i*3], '|', field[1+i*3], '|', field[2+i*3], '|')
#         print('-------------')

# draw_field(field)




# from functools import reduce

# d = [1, 2, 3, 4, 5]

# pr = reduce(lambda x, y: x*y, d)
# print (pr)

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
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


s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")