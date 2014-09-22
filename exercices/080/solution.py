# -*- coding: utf-8 -*-
Alphabet='abcdefghijklmnopqrstuvwxyz'
init=0
for i in range(len(Alphabet)):
    for j in range(init,len(Alphabet)):       
        if i!=j:
            print(Alphabet[i]+Alphabet[j])
    init=init+1
