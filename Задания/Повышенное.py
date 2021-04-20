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
    a = -x/4
    S, n = a, 0
    while math.fabs(a) > EPS:
        a *= (-x*(2*n+1))/((2*n+2)**2)
        S += a
        n += 1
    print(f"Si({x})=", S)