# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 19:15:22 2021

@author: Sarah Anne Pedersen
"""
#Sorting numbers 

def combine(numbers1,numbers2): 
    l = numbers1 + numbers2
    l.sort()
    return l 

n1 =[1,22,4,3]
n2 = [2,1,4,2]

print(combine(n1,n2))

#%% Text processing 

def compare(word): 
    word = word
    speech1 = open("obama.txt", "r", encoding = "utf-8")
    speech2 = open("biden.txt", "r", encoding = "utf-8")
    oba_count = obama(word, speech1)
    bid_count = biden(word, speech2)
    print(f"The word {word}, has been used ", oba_count, " times by obama and ", bid_count ," times by Biden")
    
    
def obama(word, speech1): 
    counter = 0
    for line in speech1.readlines(): 
        line = line.replace(",","").replace(".","")
        words = line.split(" ")
        for element in words: 
            if element == word:
                counter = counter + 1
    return counter 

def biden(word, speech2): 
    counter = 0
    for line in speech2.readlines(): 
        line = line.replace(",","").replace(".","")
        words = line.split(" ")
        for element in words: 
            if element == word:
                counter = counter + 1
    return counter


compare("us")



