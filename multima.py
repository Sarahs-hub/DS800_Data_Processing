# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 19:40:03 2021

@author: Sarah Anne Pedersen
"""

a = [[1,2,3],[3,2,1]]
b = [[3,2],[2,3],[2,1]]


a_i = len(a) # Length M of resulting matrix
a_j = len(a[0]) # Length of product computations
b_j = len(b[0]) # Length N of resulting matrix

c = [] # Resulting matrix

for i in range(a_i): # each row M in C
    row = []
    for j in range(b_j): # each col N in C
        sum = 0
        
        for n in range(a_j): # for each computation between A and B
            sum = sum + (a[i][n]*b[n][j])
            
        row.append(sum) # add result for C at i(M), j(N)
    c.append(row) 
print(c)       
