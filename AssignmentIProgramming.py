# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:55:14 2020

@author: Sarah Anne Pedersen
"""

# Assignment I Programming 

import math 
import os  
import matplotlib.pyplot as plt 




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

#%% Write norm function  
# Write a function median which takes a list as input and return the median 

def median(l): 
    l.sort()
    n = len(l)
    m =int((n)/2)
    print(l[m])
   
                       
#%% Write norm function  
        
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


#%%  
        
    
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



text = open("texts/raven.txt","r", encoding = "utf-8")
characters(text)
       
#%% Write norm function  
# Word freguency: count frequency of a word in the genesis. Viualize it in
# with matplotlib as line plot 

def count(term):
    frequency = {}
    for chapterFilename in os.listdir("genesis"): 
        chapter = open("genesis/" + chapterFilename,"r", encoding = "utf-8")
        frequency[chapterFilename] = 0
        for line in chapter.readlines():
            words = line.split(" ")
            for word in words: 
                if term == word:
                    frequency[chapterFilename] +=1

    myKeys = list(frequency.keys())
    myKeys.sort()
    
    for key in myKeys:
        print("key", key, "count", frequency[key]) 
   
    D = frequency 
    chapter = list(range(1,51))
    counts = list(D.values())
    plt.plot(chapter, counts)
    plt.ylabel('Frequency of God')
    plt.xlabel('Chapter')
    plt.xlim(0, 50)
    plt.show()
    
count("Horse")







    