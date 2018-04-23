from math import *

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
delta = pow(b, 2)-4*a*c

print("The form of a quadratic equation: {}x^2+{}x+{}".format(a, b, c))
print("Delta equals to:", delta)

if a == 0:
    print("This is not a quadratic equation!")
elif delta > 0:
    x1 = (-b - sqrt(delta))/(2*a)
    x2 = (-b + sqrt(delta))/(2*a)
    print("x1 = {} and x2 = {}".format(round(x1, 2), round(x2, 2)))
elif delta == 0:
    x1 = (-b)/(2*a)
    print("x1 = {}".format(round(x1, 2)))
elif delta < 0:
    print("No elements")