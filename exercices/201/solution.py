# -*- coding: utf-8 -*-
def is_alpha(n):
    import string
    TargChar = 0

    for i in range(len(n)):
        TargChar = 0
        for j in range(len(string.ascii_letters)):
                if n[i] == string.ascii_letters[j]:
                    TargChar = 1
        if TargChar == 0:
            return False
    if TargChar == 1:
        return True
