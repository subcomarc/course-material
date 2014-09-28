# -*- coding: utf-8 -*-
Alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(Alphabet)):
    for j in range(len(Alphabet)):
        if i != j:
            print(Alphabet[i]+Alphabet[j])
