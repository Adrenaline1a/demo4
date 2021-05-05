#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys
EPS = 1e-10
if __name__ == '__main__':
    x = float(input("Value of x? "))
    if x == 0:
        print("Illegal value of x", file=sys.stderr)
        exit(1)
    a = x
    S, n = a, 1
    while math.fabs(a) > EPS:
        k = 2 * n + 1
        a *= (-x*x*(k-2))/(k*k*2*n)
        S += a
        n += 1
    print(f"Si({x})={S}")
