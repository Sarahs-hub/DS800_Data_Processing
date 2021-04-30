# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 08:12:50 2021

@author: Sarah Anne Pedersen
"""
import math 

def norm(v): 
    sum_v = 0 
    for i in range(len(v)): 
        sum_v= sum_v + (i*i)
    return math.sqrt(sum_v)


v = [1,2,3]

print(norm(v))

#%%

def diff(A,B): 
    m = len(A)
    n = len(A[0])
    result = []
    for i in range(m):
        row = []
        for j in range(n): 
            row.append(A[i][j]-B[i][j])
        result.append(row)
    return result 

A = [[7,8],[2,10]]
B = [[1,5],[3,4]]

print(diff(A,B))
#%%
import matplotlib as plt
import numpy as np
 
# read csv file 
file = np.genfromtxt("earthquakes.csv", delimeter = ";")
#remove first row 
data = data[1:,]
#filter data 
# 1st finding rows to use, 2nd extract rows to use 
filter_data= data[:,2] >= 8
data = data[filter_data,:]
# creates column 5 as input for x axsis
x = data[:,5]
# creates column 4 as input for x axsis
y = data[:,4]
plt.scatter(x,y)
plt.show()

print(max(data[:,2]))
    
#%%
def multi(A,B): 
    m = len(A)
    n = len(A[0])
    result = []
    for i in range(m): 
        row=[]
        for j in range(n): 
            row.append(A[i][j]*B[j][i])
            

#%%Euclidan distance 
            
def distance(p,q):
    sum = 0
#need to run through the length of the list  
    dimension = len(p)
    for i in dimension: 
        # finding the difference between the 2 numbers by accessing content on i's place
        diff = q[i]-p[i]
        # adding the power of the difference to sum
        sum = sum +(diff*diff)
        
    
            