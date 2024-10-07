import math

sideValue = float(input())

roundSideValue = math.ceil(sideValue)


def square(side):
    return side * side


print("Площадь квадрата - ", square(roundSideValue))
