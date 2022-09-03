#day 3
from calendar import c
import math
from tkinter import N
age = 22
height = 164.0
comp = 1 + 2j
base = int(input("please enter the base of the triangle: "))
height = int(input("please enter the height: "))
area = 0.5 * base * height
print(f"the area of the triangle is {area}")

y2 = 10
y1 = 2 
x2 = 6
x1 = 2
m = y2 - y1 / x2 - x1
d = (((y2 - y1) ** 2) + ((x2 - x1) ** 2))**0.5
print(f"the d is {d}")

a , b , c = int(input("a : ")) , int(input("b : ")), int(input("c : "))
delta = b ** 2 - 4 * a * c
if delta > 0:
    x1 = (- b +  math.sqrt(delta)) / 2 * a
    x2 = (- b -  math.sqrt(delta)) / 2 * a
else:
    print("theres no answer!")

py_len = len("python")
dr_len = len("dragon")
print(dr_len > py_len)
print('on' in 'python' and 'on' in 'dragon')

fl_py = str(float(py_len))

num = int(input("enter the num"))
if num%2 == 0:
    print("the number is even")
else:
    print("the number is odd")

print((7 // 3) is int(2.7))
print('10' is 10)
print(int(9.8) is 10)




