# -*- coding: utf-8 -*-
import is_prime   
Primes=[]
for i in range(10000,10050): 
    if is_prime.is_prime(i):
        Primes=Primes+[i]
print(Primes)
    