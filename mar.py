# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 17:49:27 2021

@author: Sarah Anne Pedersen
"""

## even function 


def even(v): 
    sum =0
    for element in v: 
        sum = sum + element
    return sum % 2 == 0
       
#%% Write norm function  
    
def AND(A,B): 
    m = len(A)
    n = len(A[0])
    result = []
    for i in range(m):
        row = []
        for j in range(n):
            if A[i][j] == 1 and B[i][j] == 1: 
                row.append(1)
            else:
                row.append(0)
        result.append(row)
    return result 




A = [[1,0,1],[1,0,0]]
B = [[1,0,1],[0,0,1]]

print(AND(A,B))

#%% modified 

import numpy as np
import matplotlib.pyplot as plt

def magnitude(yearMin,yearMax):
    data = np.genfromtxt("EarthQuakes in Greece.csv", delimiter=',')
    data = data[1:,] 
    chart = []
    x = []
    for year in range(yearMin,yearMax): 
        sum_year = 0
        filter_data = data[:,0] == year
        data_year = data[filter_data,-1]
        for magnitude in data_year: 
            sum_year = sum_year + magnitude
        chart.append(sum_year)
        x.append(year)
    plt.plot(x,chart)
    plt.locator_params(axis="both", integer = True, tight=True)
    plt.show()
   
        


print(magnitude(1902,1905))