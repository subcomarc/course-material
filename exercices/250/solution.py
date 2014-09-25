# -*- coding: utf-8 -*-
def draw_n_squares(n):
    part1 = '+---+' * n
    part2 = '|   |' * n
    part3 = '+---+' * n
#    s = part1 * n
    for i in range(n):
        print(part1)
        print(part2)
        print(part3)
