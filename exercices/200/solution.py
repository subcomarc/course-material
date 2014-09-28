# -*- coding: utf-8 -*-
import math


def is_prime(n):
    Prime = 1
    TargNum = 1
    SecNum = math.ceil(math.sqrt(n))
    if n % 2 != 0:
        if n % 3 != 0:
            if n % 5 != 0:
                for i in range(7, SecNum+1):
                    if n % i == 0:
                        TargNum = 0
            else:
                TargNum = 0
        else:
            TargNum = 0
    else:
        TargNum = 0
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n == 3:
        return True
    elif n == 5:
        return True
    else:
        return TargNum == Prime
