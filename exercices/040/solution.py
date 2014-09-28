# -*- coding: utf-8 -*-
EndResult = 0
for i in range(101):
    if int(i) % 2 == 0:
        EndResult = EndResult + int(i)
print(EndResult)
