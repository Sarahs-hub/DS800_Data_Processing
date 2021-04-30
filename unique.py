# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:08:48 2020

@author: Sarah Anne Pedersen
"""

# Write a unique list of objects l & return a sub-list that contains items in 
# which only occurs once 

def unique(l): 
    counter = {}
    newList = []
    
    for i in l: 
        if i in counter: 
            counter[i]= counter[i] + 1
        else: 
            counter[i] = 1
    for key,value in counter.items():
        if value == 1: 
            newList.append(key)
    return newList