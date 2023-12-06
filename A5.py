# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 23:54:35 2023

@author: sahil
"""


lines = []
with open('Q5.txt') as f:
    for line in f:
        lines.append(line[:-1])
n = len(lines)

# Part 1
for line in lines:
    if line.startswith('seeds:'):
        curr_arr = list(map(int, line.replace('seeds: ', '').split(' ')))
        
    elif line.endswith(' map:'):
        from_m, to_m = line.replace(' map:', '').split('-to-')
        map_dict = {}
    
    elif len(line) > 0:
        st_dest, st_source, n = list(map(int, line.split(' ')))
        map_dict[(st_source, st_source+n-1)] = st_dest

    elif len(line) == 0:
        def _f(map_dict, c):
            for k, v in map_dict.items():
                if k[0] <= c <= k[1]:
                    return v + (c-k[0])
                return c    
        curr_arr = [_f(map_dict, c) for c in curr_arr]        
print(min(curr_arr))
# 40283135

# Part 2
for line in lines:
    if line.startswith('seeds:'):
        #curr_arr = list(map(int, line.replace('seeds: ', '').split(' ')))
        tmp = list(map(int, line.replace('seeds: ', '').split(' ')))
        curr_arr = []
        for i in range(len(tmp) // 2):
            curr_arr.append((tmp[2*i],tmp[2*i]+tmp[2*i+1]-1))
        
    
    
    elif line.endswith(' map:'):
        from_m, to_m = line.replace(' map:', '').split('-to-')
        map_dict = {}
    
    elif len(line) > 0:
        st_dest, st_source, n = list(map(int, line.split(' ')))
        map_dict[(st_source, st_source+n-1)] = (st_dest, st_dest+n-1)

    elif len(line) == 0:
        def _f2(map_dict, c):
            out = []    
            while c[0] < c[1]:
                update_flag = False
                for k, v in map_dict.items():
                    if (k[0] <= c[0]) and (c[1] <= k[1]):
                        update_flag = True
                        out.append( (v[0]+c[0]-k[0], v[0]+c[1]-k[0]) )
                        c = (0, -1)

                    elif k[0] <= c[0] <= k[1]:
                        update_flag = True                        
                        out.append( (v[0] + (c[0]-k[0]), v[1] ) )
                        c = (k[1]+1, c[1])
                    
                    elif k[0] <= c[1] <= k[1]:
                        update_flag = True
                        out.append( (v[0], v[0]+c[1]-k[0]) )
                        c = (c[0], k[0]-1)

                if not update_flag:                    
                    out.append( (c[0], c[1] ))
                    c =( c[0], -1)
            return out

        curr_arr = sum([_f2(map_dict, c) for c in curr_arr], [])
        
print(min([c[0] for c in curr_arr]))
# 11554135





