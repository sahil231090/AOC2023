# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 00:41:50 2023

@author: sahil
"""


from math import gcd

lines = []
with open('Q8.txt') as f:
    for line in f:
        lines.append(line[:-1])
n = len(lines)


map_d = {}
node_list = []
for idx, line in enumerate(lines):
    if idx == 0:
        instr = list(line)
    if idx > 1:
        node, nxt = line.split(' = ' )
        map_d[node] = tuple(nxt[1:-1].split(', '))
        node_list.append(node)

hist = set('AAA')
curr_loc = 'AAA'
counter = 0
instruct_idx = 0
while curr_loc != 'ZZZ':
    
    if instruct_idx == len(instr):
        instruct_idx = 0
    
    ins = instr[instruct_idx]
    if ins == 'L':
        curr_loc =  map_d[curr_loc][0]
    elif ins == 'R':
        curr_loc =  map_d[curr_loc][1]
    counter += 1
    instruct_idx += 1
print(counter)


init_nodes = [n for n in node_list if n[-1]=='A']
counters = [0 for n in init_nodes]
for ni, node in enumerate(init_nodes):
    instruct_idx = 0
    
    while node[-1] !='Z':
        
        if instruct_idx == len(instr):
            instruct_idx = 0
    
        ins = instr[instruct_idx]
        if ins == 'L':
            node =  map_d[node][0]
        elif ins == 'R':
            node =  map_d[node][1]
        
        counters[ni] += 1
        instruct_idx += 1
lcm = 1
for i in counters:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)
