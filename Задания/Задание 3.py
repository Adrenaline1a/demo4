#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x=0
if __name__ == '__main__':
    for i in range(100):
        if (i>20 and i%3==0):
            x+=i
print("Сумма чисел, удовлетворяющих условиям, равна:", x)