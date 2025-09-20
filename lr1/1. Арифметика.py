# 1. арифметика
import math

a = int(123)
b = float(213)
r = 5
s_krug = math.pi * (r**2)

print(a + b, a - b, a * b, a / b, type(a / b))
print("Площадь круга: ", round(s_krug, 2))