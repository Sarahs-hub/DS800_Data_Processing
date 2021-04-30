# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:10:08 2020

@author: Sarah Anne Pedersen
"""
import os  
import matplotlib.pyplot as plt 

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
    
count("horse")
