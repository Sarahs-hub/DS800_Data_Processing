# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:09:17 2020

@author: Sarah Anne Pedersen
"""
import os  

# Write fucntion which assign each word to dictionary from textfile & return 
# the dictionaries alphabetically sorted
    
def characters(textfile): 
    counter = {}
    
    for line in textfile.readlines():
        for char in line: 
            if char in counter: 
                counter[char] +=1
            else: 
                counter[char] = 1

    myKeys = list(counter.keys())
    myKeys.sort()
    
    for key in myKeys:
        print("key", key, "count", counter[key])    