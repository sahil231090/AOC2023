# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:05:29 2023

@author: sahil
"""

import os
import numpy as np
import bisect 


#a = [1, 2, 4, 5] 
#bisect.insort(a, 3) 
#print(a)
sum_ = 0
sum_2 = 0

_three_digits = ['one', 'two', 'six',]
_four_digits = ['four', 'five', 'nine']
_five_digits = ['three', 'seven', 'eight']

# Part 1
with open('Q1.txt') as f:
    for line in f:
        tmp = [c for c in line if c in map(str, range(10)) ]
        s = 10*int(tmp[0]) + int(tmp[-1])
        print(s)
        sum_ +=s
        
# Part 2
with open('Q1.txt') as f:
    for line in f:
        digits_in_line = []
        for idx, c in enumerate(line):
            if c.is_digit():
                digits_in_line.append(int(c))
                break
            elif line[idx:idx+3] in _three_digits:
                if line[idx:idx+3] == 'one':
                    digits_in_line.append(1)
                    break
                elif line[idx:idx+3] == 'two':
                    digits_in_line.append(2)
                    break
                elif line[idx:idx+3] == 'six':
                    digits_in_line.append(6)
                    break     
            elif line[idx:idx+4] in _four_digits:
                if line[idx:idx+4] == 'four':
                    digits_in_line.append(4)
                    break
                elif line[idx:idx+4] == 'five':
                    digits_in_line.append(5)
                    break
                elif line[idx:idx+4] == 'nine':
                    digits_in_line.append(9)
                    break     
            elif line[idx:idx+5] in _five_digits:
                if line[idx:idx+5] == 'three':
                    digits_in_line.append(3)
                    break
                elif line[idx:idx+5] == 'seven':
                    digits_in_line.append(7)
                    break
                elif line[idx:idx+5] == 'eight':
                    digits_in_line.append(8)
                    break
        
        s = 10*int(digits_in_line[0]) + int(digits_in_line[-1])
        print(s)
        sum_2 +=s
        