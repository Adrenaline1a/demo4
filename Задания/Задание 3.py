#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    x = 0
    i = 21
    while i < 100:
        if i % 3 == 0:
            x += i
        i += 1
    print("Сумма чисел, удовлетворяющих условиям, равна:", x)
