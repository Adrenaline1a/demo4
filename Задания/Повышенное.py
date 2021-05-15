#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
EPS = 1e-10
if __name__ == '__main__':
    x = float(input("Value of x? "))
    a = x
    S, n = a, 0
    while math.fabs(a) > EPS:
        a *= (-1*(x**2)*(2*n+1))/(((2*n+3)**2)*(2*n+2))
        S += a
        n += 1
    print(f"Si({x})={S}")
