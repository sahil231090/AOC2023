# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 23:56:28 2023

@author: sahil
"""


from copy import  copy



lines = []
syms = set()
with open('Q3.txt') as f:
    for line in f:
        lines.append(line[:-1])
        syms = syms.union(set(line[:-1]))
n = len(lines)
m = len(line)-1
syms = syms - set(map(str, range(10))) - set(['.'])
nums = []
ch_groups = []

in_num = False
st_idx, st_jdx, ed_jdx, chr_group = None, None, None, []
special_sym = '*'



def _check_num(lines, st_idx, st_jdx, ed_jdx):
    num_is_valid = False
    chr_group = []

    # Top Row
    if st_idx > 0:
        # Top-left
        if st_jdx > 0:
            if lines[st_idx-1][st_jdx-1] in syms:
                num_is_valid = True
                chr_group.append((lines[st_idx-1][st_jdx-1], 'TL', st_idx-1, st_jdx-1))
        # Top Middle
        for kdx in range(st_jdx, ed_jdx+1):
            if lines[st_idx-1][kdx] in syms:
                num_is_valid = True
                chr_group.append((lines[st_idx-1][kdx], 'TM', st_idx-1, kdx))
        # Top-Right
        if ed_jdx < m-1:
            if lines[st_idx-1][ed_jdx+1] in syms:
                num_is_valid = True
                chr_group.append((lines[st_idx-1][ed_jdx+1], 'TR', st_idx-1, ed_jdx+1))
    # Middle
    if st_jdx > 0:
        # Middle Left
        if lines[st_idx][st_jdx-1] in syms:
            num_is_valid = True
            chr_group.append((lines[st_idx][st_jdx-1], 'ML', st_idx, st_jdx-1))
        
    if ed_jdx < m-1:  
        # Middle Right
        if lines[st_idx][ed_jdx+1] in syms:
            num_is_valid = True
            chr_group.append((lines[st_idx][ed_jdx+1], 'MR', st_idx, ed_jdx+1))
    
    # Bottom
    if st_idx < m-1:
        # Top-left
        if st_jdx > 0:
            if lines[st_idx+1][st_jdx-1] in syms:
                num_is_valid = True
                chr_group.append((lines[st_idx+1][st_jdx-1], 'BL', st_idx+1, st_jdx-1))
        # Top Middle
        for kdx in range(st_jdx, ed_jdx+1):
            if lines[st_idx+1][kdx] in syms:
                num_is_valid = True
                chr_group.append((lines[st_idx+1][kdx], 'BM', st_idx+1, kdx))
        # Top-Right
        if ed_jdx < m-1:
            if lines[st_idx+1][ed_jdx+1] in syms:
                num_is_valid = True
                chr_group.append((lines[st_idx+1][ed_jdx+1], 'BR', st_idx+1, ed_jdx+1)) 
    
    return num_is_valid, chr_group

for idx, line in enumerate(lines):
    
    if in_num:
        ed_jdx = m-1
        potential_num = int(lines[st_idx][st_jdx:ed_jdx+1])
        in_num = False
        # Check
        num_is_valid, chr_group = _check_num(lines, st_idx, st_jdx, ed_jdx)
        if num_is_valid:
            nums.append(potential_num)
            ch_groups.append(chr_group)
        
    
    
    for jdx, c in enumerate(line):
        if not c.isdigit():            
            if in_num:                
                ed_jdx = copy(jdx)-1
                potential_num = int(lines[st_idx][st_jdx:ed_jdx+1])
                in_num = False
                # Check
                num_is_valid, chr_group = _check_num(lines, st_idx, st_jdx, ed_jdx)
                if num_is_valid:
                    nums.append(potential_num)
                    ch_groups.append(chr_group)
                
        elif c.isdigit():
            if not in_num:
                
                st_idx = copy(idx)
                st_jdx = copy(jdx)
                in_num = True

pair_dict = {}
for ix, (n_i, ch_group) in enumerate(zip(nums, ch_groups)):
    for c, _, ci, cj in ch_group:
        if c == special_sym:

            for jx, (n_j, ch2_group) in enumerate(zip(nums, ch_groups)):
                if ix == jx:
                    continue
                for c2, _, c2i, c2j in ch2_group:
                    if (c2i == ci) and (cj == c2j) and ( (jx,ix) not in pair_dict ):
                        pair_dict[(ix, jx)] = (n_i, n_j, n_i*n_j)


print(sum(nums)) #527144
print(sum([v[2] for k,v in pair_dict.items()])) #81463996



