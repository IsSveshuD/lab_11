#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fum(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return fum(m - 1, 1)
    if m > 0 and n > 0:
        return fum(m - 1, fum(m, n - 1))


m = int(input("m = "))
n = int(input("n = "))

if __name__ == '__main__':
    print(fum(m, n))
