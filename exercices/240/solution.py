# -*- coding: utf-8 -*-
import is_prime
import itertools
import sys
for i in itertools.count(100000000):   
    if is_prime.is_prime(i):
        print(i)
        sys.exit()
  