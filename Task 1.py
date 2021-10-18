#!/usr/bin/env python 3
# -*- coding: utf-8 -*-


def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("factorial(10)", setup="from __main__ import factorial"))
