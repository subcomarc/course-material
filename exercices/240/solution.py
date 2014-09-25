# -*- coding: utf-8 -*-
FibList = [1, 2, 3]
for i in range(3, 10):
    FibList.append(FibList[i-2] + FibList[i-1])
print('{}.'.format(', '.join(str(e) for e in FibList)))
