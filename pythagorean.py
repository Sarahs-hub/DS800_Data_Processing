# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:07:11 2020

@author: Sarah Anne Pedersen
"""
import math 
# Write a program that solves the Pythagorean theorem. 
#The user should give the input & the program should solve the unknown side 
#Pythagorean theorem is known as a**2+b**2=c**2

def pythagorean():
    a = input("How long is side a in centimeters? if unknown write: ? ")
    b = input("How long is side b in centimeters? if unknown write: ? ")
    c = input("How long is side c in centimeters? if unknown write: ? ")
    if a == "?": 
        print("a equals: ", math.sqrt((int(c)**2)-(int(b)**2)))
    elif b == "?":
        print("b equals: ", math.sqrt((int(c)**2)-(int(a)**2)))
    elif c == "?": 
        print("c equals: ", math.sqrt((int(a)**2)+(int(b)**2)))