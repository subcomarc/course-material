# -*- coding: utf-8 -*-
def draw_n_squares(n):
    opener1 = '+---+'
    opener2 = '|   |'
    middle1 = '---+' * (n-1)
    middle2 = '   |' * (n-1)
#    s = part1 * n
    for i in range(n):
            print(opener1+middle1)
            print(opener2+middle2)
    print(opener1+middle1)
