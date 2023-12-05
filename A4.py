# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 23:54:50 2023

@author: sahil
"""

import numpy as np

lines = []
syms = set()
sum_ = 0
with open('Q4.txt') as f:
    for line in f:
        line = line[:-1]
        lines.append(line)


n = len(lines)
weight = np.ones(n)
for idx, line in enumerate(lines):
        card_num, tick_info = line.split(':')
        
        card_num = int(card_num.replace('Card ', ''))
        win_num, your_num = tick_info.split('|')
        win_num = set(map(int, filter(lambda x: len(x) > 0, win_num.split(' '))))
        your_num = set(map(int, filter(lambda x: len(x) > 0, your_num.split(' '))))
     
        got_num = win_num.intersection(your_num)
        if len(got_num)>0:
            sum_ += 2**(len(got_num) -1)
            weight[idx+1:min(n,idx+1+len(got_num))] += weight[idx]
print(sum_)             # Part 1 : 21959
print(int(sum(weight))) # Part 2 : 5132675
