# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141

import math
from math import pi

d = int(input('Введите желаемое количество знаков после запятой  '))

print(round(pi, d))
