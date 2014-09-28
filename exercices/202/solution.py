# -*- coding: utf-8 -*-
def starts_with(A, B):
    Letter = 1
    TargChar = 1
    if len(A) > len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            TargChar = 0
    return (Letter == TargChar)
