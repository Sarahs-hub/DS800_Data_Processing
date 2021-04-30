# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 19:02:26 2021

@author: Sarah Anne Pedersen
"""
#import python file with distances 
import distances as d
#import math lib
import math 

def distance(p,q): 
    #create variable for sum
    sum_dis = 0
    #save length of p 
    dim =len(p)
    #run through every element in the range of dim
    for i in range(dim):
        #finds the difference between the number of p & q at each index
        diff = q[i]-p[i]
        #adds sum to sum + the power of the differnce between p&q
        sum_dis = sum_dis + (diff * diff)
        # the sum is squared by math
    distance = math.sqrt(sum_dis)
    return distance 

def shortest():
    #selecting the list called points from d file and save it in data 
    data = d.points
    #sets the check to max in order to save small input in var.
    min_dist = float("inf")
    #Runs through all indexes in data
    for i in range(len(data)):
        # runs through and look at the next element in data after i 
        for j in range(i+1,len(data)):
            #calls the funktion distance on entry i & j from data
            dist = distance(data[i],data[j])
            # the returned distance of the function is < then min_dist, /
            # then it is saved in the check variable
            if dist < min_dist: 
                min_dist = dist
    return min_dist 


def longest():
    data = d.points
    max_dist = 0
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            dist = distance(data[i],data[j])
            if dist > max_dist: 
                max_dist = dist
    return max_dist 

print(shortest(), longest())

#%%

def start():
    #create set to ensure all elements in the set is unique. Set also support set operations
    unique = set()   
    # open txt file  and saves in speech
    speech = open("trump-capitol-speech.txt","r", encoding = "utf-8")
    # run through line for line and read content
    for line in speech.readlines():
        #Cleaning lines
        line = line.replace(",","").replace(".","")
        # splitting lines into words/elements for every space between
        words = line.split(" ")
        # run through every word/element in list of words
        for word in words: 
            # if element starts with "fight", then it is added to our set unique 
            if word.startswith("fight"): 
                unique.add(word)
    return unique

print(start())

#%%


def followI():
    # create boolean to check for i 
    i = False
    # create set to ensure unigueness
    unique = set()   
    # open and save speeach in speech
    speech = open("trump-capitol-speech.txt","r", encoding = "utf-8")
    # cleaning speech
    for line in speech.readlines():
        line = line.replace(",","")
        line = line.replace(".","")
        #Splitting lines to words
        words = line.split(" ")
        for word in words:
            # create condition for i needs to be true, to add word 
            if i == True: 
                unique.add(word)
            # set condition word most be "I" for i to be true.
            if word == "I": 
                i = True
                # i is set to False
            else: 
                i = False
    return unique
            

print(followI())

#%%
def ends():
    unique = set()   
    speech = open("trump-capitol-speech.txt","r", encoding = "utf-8")
    for line in speech.readlines():
        line = line.replace(",","")
        line = line.replace(".","")
        words = line.split(" ")
        for word in words: 
            if word.endswith("ing"): 
                unique.add(word)
    return unique


print(ends())

#%%
import numpy as np

def home_wins():
    #create counter
    total_wins = 0 
    #load data 
    data = np.genfromtxt("Football.csv", delimiter=',')
    #saves all data from 1st (2nd) row and onwards 
    data = data[1:,]
    # extract all rows for column 4
    home = data[:,4]
    # extract all rows for column 5
    away = data[:,5]
    # runs through all elements in length of home
    for i in range(len(home)):
        # saves index content in var. for later use
        home_score = home[i]
        away_score = away[i]
        # checks if the home score > away score
        if home_score > away_score:
            total_wins = total_wins + 1
    return total_wins

print(home_wins())


#%%

def away_wins(): 
    data = np.genfromtxt("Football.csv", delimiter=',', names = True, dtype = None, encoding = "utf-8")
    total_away_win = 0
    for row in data: 
        if row["HomeTeamGoals"] < row["AwayTeamGoals"]: 
            total_away_win = total_away_win + 1
    return total_away_win

print(away_wins())

#%%

import numpy as np

bif_in_odn = 0 
data = np.genfromtxt("Football.csv", delimiter=',', names = True, dtype = None, encoding = "utf-8")
#run through all rows in data
for row in data: 
    # check the content of each rows column number and see if condition sticks
    if row[3] == "Brondby" and row[2] == "Odense" and row[-1] > row[-2]:
        bif_in_odn = bif_in_odn + 1
print(bif_in_odn)
        
#%%
import numpy as np

draw = 0 
data = np.genfromtxt("Football.csv", delimiter=',', names = True, dtype = None, encoding = "utf-8")
for row in data: 
    if (row[3] == "Midtjylland" or row[2] == "Midtjylland") and row[-1] == row[-2]:
        draw = draw +1
print(draw)
        
#%%
import numpy as np
data = np.genfromtxt("Football.csv", delimiter=',', names = True, dtype = None, encoding = "utf-8")

goals = 0 

for row in data:
    away_team = row["AwayTeam"]
    home_team = row["HomeTeam"]
    away_goal = row["AwayTeamGoals"]
    home_goal = row["HomeTeamGoals"]
    if home_team == "FC Copenhagen" and home_goal: 
        goals = goals + home_goal
    if away_team == "FC Copenhagen" and away_goal:
        goals = goals + away_goal
        
print(goals)

#%%

import json

#open & saves json fil 
file = open('dbl.json', encoding='UTF-8')
dbl = json.load(file)

#function checks if officer is in element and return true or false
def is_officer(o): 
    for element in o:
        if "officer" in element.lower(): 
            return True
    return False 
        

def officers(dbl):
    names = []
    #run through all elements 
    for element in dbl:
    # checks if function returns true & if so, append name to list
        if is_officer(element["o"]) == True: 
            names.append(element["name"])
    return names 
    
print(officers(dbl))
#%%

import json

file = open('dbl.json', encoding='UTF-8')
dbl = json.load(file)


def is_painter(o): 
    for element in o:
        if "painter" in element.lower(): 
            return True
    return False 
        

def get_age(l): 
    if "-" not in l or len(l) < 8:
        return float('inf')
    life= l.split("-")
    year_one = int(life[0])
    year_two = int(life[1])
    return year_two-year_one

def young(dbl):
    names = []
    for element in dbl:
        if is_painter(element["o"]) == True and get_age(element["l"]) < 30: 
            names.append(element["name"])
    return names 
    
print(young(dbl))
#%%
import json

file = open('dbl.json', encoding='UTF-8')
dbl = json.load(file)

def women(dbl):
    names = []
    for element in dbl:
        if element["g"] == "f" and element["y"] < 1900: 
            names.append(element["name"])
    return names 
    
print(women(dbl))
