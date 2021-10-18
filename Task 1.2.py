#!/usr/bin/env python 3
# -*- coding: utf-8 -*-


def factorial(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("factorial(10)", setup="from __main__ import factorial"))
