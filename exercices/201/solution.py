# -*- coding: utf-8 -*-
def is_alpha(n):
    import string    
    Letter=1;
    TargChar=0; 

    for i in range(len(n)):
        for j in range(len(string.ascii_letters)):                
                if n[i]==string.ascii_letters[j]:
                    TargChar=1
                
    print(Letter==TargChar)
        