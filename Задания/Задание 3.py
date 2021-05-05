#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    x = 0
    for i in range(100):
        if i > 20 and i % 3 == 0:
            x += i
    print("Сумма чисел, удовлетворяющих условиям, равна:", x)
