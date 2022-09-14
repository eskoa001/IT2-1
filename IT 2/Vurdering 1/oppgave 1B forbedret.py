# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 12:39:07 2022

@author: eiaaa001
"""

"""
The task which the program is based on:
You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.
"""

#Importing RegEx for Python
import re

coordinates = [0,0]   #Array for the coordinates

def is_valid_walk(array): #Defining the function that executes the route
    if len(array) != 10:     #Checking if the route is 10 minutes
        return False
    else:
        for i in range(len(array)):  #Executing route
            if array[i] == "n":
                coordinates[1]+=1
            elif array[i] == "s":
                coordinates[1]-=1
            elif array[i] == "e":
                coordinates[0]+=1
            elif array[i] == "w":
                coordinates[0]-=1
        if coordinates[0]==0 & coordinates[1]==0:   #Checking if start and end point is the same
            return True
        else:
            return False

def check_format(string):   #Checking the input format
    x = re.findall("[nsew]", string)    #Checking if there are any other characters than n, s, e or w.
    if len(x)==len(string):     #If input is ok, proceed to is_valid_walk. If not, inform the user.
        arr = string.split()
        print(is_valid_walk(arr))
    else:
        print("Inputen har ikke riktig format.")

print("Legg inn et sett med koordinater som en sammenhengende string for å se om det er godkjent. Eks: nsew") #Input 
inn = input()
check_format(inn)
    

