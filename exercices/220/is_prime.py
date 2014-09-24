# -*- coding: utf-8 -*-
def is_prime(n):
    Prime=1;
    TargNum=1;

    for i in range(2,n-1):
        if n%i==0:
            TargNum=0    
#    print(Prime==TargNum)
    if Prime==TargNum:
        return n    