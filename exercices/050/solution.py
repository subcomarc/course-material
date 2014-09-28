# -*- coding: utf-8 -*-
MySum = 0
for i in range(1000):
    if int(i) % 3 == 0 or int(i) % 5 == 0:
        MySum = MySum + int(i)
print(MySum)
