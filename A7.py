# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 00:30:57 2023

@author: sahil
"""

import os
import numpy as np
import bisect 
from collections import defaultdict
from itertools import product



lines = []
with open('Q7.txt') as f:
    for line in f:
        lines.append(line[:-1])
n = len(lines)

values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}


def check_five_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [5]:
        return True
    return False

def check_four_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,4]:
        return True
    return False

def check_full_house(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [2,3]:
        return True
    return False

def check_three_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,1,3]:
        return True
    return False

def check_two_pair(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,2,2]:
        return True
    return False

def check_one_pair(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,1,1,2]:
        return True
    return False

def check_high_card(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,1,1,1,1]:
        return True
    return False

hand_dict = {9:check_five_of_a_kind, 
             8:check_four_of_a_kind, 
             7:check_full_house, 
             6:check_three_kind, 
             5:check_two_pair, 
             4:check_one_pair, 
             3:check_high_card,
             }


def hand_val(hand):
    val_arr = []
    val_ = 0
    denom = 10000000000
    for k, v in hand_dict.items():
        if v(hand):
            val_arr.append(k)
            val_ += k*10000000000
    for h in hand:
        denom /= 100
        val_arr.append(values[h])
        val_ += values[h] * denom
    return int(val_)

    

cards = [line.split(' ')[0] for line in lines]
bids = list(map(int, [line.split(' ')[1] for line in lines]))
tmp = sorted(cards, key=hand_val)
ranks = [tmp.index(i)+1 for i in cards]
print(sum([a*b for a,b in zip(ranks, bids)]))

## Part2

values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":1, "Q":12, "K":13, "A":14}
non_js = [k for k,_ in values.items() if k != 'J']

def _build_hands(hand):

    count_js = sum([k=='J' for k in hand])
    if count_js == 0:
        return hand
    max_hand = ''
    max_hand_val = 0
    for arr in list(product((*[non_js]*count_js))):
        tmp_hand_arr = []
        arr_idx = 0
        for h in hand:
            if h != 'J':
                tmp_hand_arr.append(h)
            else:
                tmp_hand_arr.append(arr[arr_idx])
                arr_idx += 1
        tmp_val = hand_val(tmp_hand_arr)
        if tmp_val > max_hand_val:
            max_hand = ''.join(tmp_hand_arr)
            max_hand_val = tmp_val
    return max_hand
  

def hand_val2(hand, og_hand):
    val_arr = []
    val_ = 0
    denom = 10000000000
    for k, v in hand_dict.items():
        if v(hand):
            val_arr.append(k)
            val_ += k*10000000000
    for h in og_hand:
        denom /= 100
        val_arr.append(values[h])
        val_ += values[h] * denom
    return int(val_)      


#251224870
cards = [line.split(' ')[0] for line in lines]
max_cards = [_build_hands(hand) for hand in cards]
bids = list(map(int, [line.split(' ')[1] for line in lines]))
vals = [hand_val2(hand, og_hand) for hand,og_hand in zip(max_cards, cards)]
tmp = sorted(vals)
ranks = [tmp.index(i)+1 for i in vals]
print(sum([a*b for a,b in zip(ranks, bids)]))