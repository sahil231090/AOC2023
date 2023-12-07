# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 23:54:34 2023

@author: sahil
"""


times = [44, 80, 65, 72]
distances = [208,   1581,   1050,   1102]
mul_ = 1
for t, d in zip(times, distances):
    c = 0
    for i in range(1, t):
        t_l = t - i
        d_t = i*t_l
        if d_t > d:
            c += 1
    mul_ *= c
print(mul_)

t = 44_806_572
d = 208_158_110_501_102

lb = 0
for i in range(1, t):
    t_l = t - i
    d_t = i * t_l
    if d_t > d:
        lb = i
        break

print(t-2*lb+1)
