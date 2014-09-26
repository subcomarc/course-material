# -*- coding: utf-8 -*-
import math
import numpy as np


def euclidean(a, b):
    Dtemp = 0
    D = 0
    for i in range(len(a)):
        Dtemp = Dtemp + (b[i]-a[i])**2
    D = Dtemp**0.5
    print(D)


def opt_euclidean(a, b):
    Dtemp = 0
    D = 0
    for i in range(len(a)):
        Dtemp = Dtemp + math.pow((b[i]-a[i]), 2)
    D = math.sqrt(Dtemp)
    print(D)


def np_euclidean(a, b):
    Dtemp = 0
    D = 0
    for i in range(len(a)):
        Dtemp = Dtemp + np.power((b[i]-a[i]), 2)
    D = np.sqrt(Dtemp)
    print(D)
