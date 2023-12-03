# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 23:57:20 2023

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
p1 = {'red': 12, 'green': 13, 'blue': 14}
with open('Q2.txt') as f:
    for line in f:
        'Game 1: 1 green, 2 red, 6 blue; 4 red, 1 green, 3 blue; 7 blue, 5 green; 6 blue, 2 red, 1 green'
        game_num, data = line[:-1].split(':')
        game_num = int(game_num.replace('Game ', ''))
        data_list = data.split(';')
        col_list = []
        data_dict = {}
        possible_flag = True
        min_dict = {'red': 0, 'blue': 0, 'green': 0}
        for idx, d in enumerate(data_list):
            c_dict = {'red': 0, 'blue': 0, 'green': 0}
            for d2 in d.split(','):
                k_n, k = d2[1:].split(' ')
                k_n = int(k_n)
                c_dict[k] = k_n
            data_dict[(game_num, idx)] = c_dict

            if c_dict['red'] > p1['red']:
                possible_flag = False
            if c_dict['green'] > p1['green']:
                possible_flag = False
            if c_dict['blue'] > p1['blue']:
                possible_flag = False
            
            min_dict['red'] = max(min_dict['red'] , c_dict['red'])
            min_dict['green'] = max(min_dict['green'] , c_dict['green'])
            min_dict['blue'] = max(min_dict['blue'] , c_dict['blue'])
            
        power_game = min_dict['red']*min_dict['green']*min_dict['blue']
        sum_2 += power_game

        if possible_flag:
            sum_ += game_num

print(sum_)
print(sum_2)
