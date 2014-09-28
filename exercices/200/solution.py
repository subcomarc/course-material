# -*- coding: utf-8 -*-
def is_prime(n):
    Prime = 1
    TargNum = 1

    for i in range(2, n-1):
        if int(n) % int(i) == 0:
            TargNum = 0
    print(Prime == TargNum)
