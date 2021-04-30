# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:08:09 2020

@author: Sarah Anne Pedersen
"""

# Write a function median which takes a list as input and return the median 

def median(l): 
    l.sort()
    n = len(l)
    m =int((n)/2)
    print(l[m])