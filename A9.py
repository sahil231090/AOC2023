# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 00:24:26 2023

@author: sahil
"""


import numpy as np
from copy import copy


sum_ = 0
sum_2 = 0
lines = []
with open('Q9.txt') as f:
    for line in f:
        lines.append(line[:-1])
n = len(lines)


map_d = {}
node_list = []

part1, part2 = 0,0
for idx, line in enumerate(lines):

    arr = np.array(list(map(np.int64, line.split())))
    arr_list = [copy(arr)]
    while np.sum(np.abs(arr)) > 0:
        arr = np.diff(arr)
        arr_list.append(copy(arr))
    
    new_vals = np.zeros(len(arr_list))
    new_vals2 = np.zeros(len(arr_list))
    
    for i in list(range(0, len(arr_list)-1))[::-1]:
        new_vals[i] = new_vals[i+1] +  arr_list[i][-1]
        new_vals2[i] = -1*new_vals2[i+1] + arr_list[i][0]
        
    sum_ += int(new_vals[0])
    sum_2 += int(new_vals2[0])
    

print(int(sum_)) #: 1877825184
print(int(sum_2)) #: 1108

