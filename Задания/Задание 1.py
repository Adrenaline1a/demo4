#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
if __name__ == '__main__':
    n = float(input("Введите n: "))
    k = n // 7
    r = n % 7
    if r == 0:
        print('n =  7 * ', k)
    else:
        print('n = 7 * ', k, " + ", r)
exit(1)