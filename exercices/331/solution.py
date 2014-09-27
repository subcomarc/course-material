# -*- coding: utf-8 -*-
digits = open('digit')
TargCiph = []
BestCiph = []
Rounds = 0
Result = 0
TempRes = 0
for line in digits:
    for d in range(len(line)-12):
        for p in range(13):
            TargCiph.append(line[d + p])
        Result = 1
        TargCiph = [int(h) for h in TargCiph]
        for i in TargCiph:
            Result = Result*i
            if Result > TempRes:
                TempRes = Result
                BestCiph = TargCiph
        TargCiph = []
print(TempRes)
digits.close()
