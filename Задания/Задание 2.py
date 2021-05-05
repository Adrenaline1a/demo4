#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
if __name__ == '__main__':
    a = float(input("Введите число а:"))
    b = float(input("Введите число b:"))
    c = float(input("Введите число c:"))
    a1 = math.fabs(a)
    b1 = math.fabs(b)
    c1 = math.fabs(c)
    if a1 >= 4:
        print("a=", a)
    if b1 >= 4:
        print("b=", b)
    if c1 >= 4:
        print("c=", c)
    else:
        print("Нет чисел, удовлетворяющих условию")
