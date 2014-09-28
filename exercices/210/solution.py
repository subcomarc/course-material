# -*- coding: utf-8 -*-
import is_prime
SumMe = 0
for i in range(1000):
    if is_prime.is_prime(i):
        SumMe = SumMe + i
print(SumMe)
