#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
if __name__ == '__main__':
    a = float(input("Введите число а:"))
    b = float(input("Введите число b:"))
    c = float(input("Введите число c:"))
    a = math.fabs(a)
    b = math.fabs(b)
    c = math.fabs(c)
    list = [a, b, c]
    for i in list:
        if i>=4:
            print(i)
        else:
            print('Не удовлетворяет условию')
