#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:43:51 2024

@author: sriram
"""

# CS1210: Project 2 Phase 1 [5 functions to complete]
###############################################################################
# Complete the signed() function, certifying that:
# 1) the code below is entirely your work, and
# 2) it has not been shared with anyone outside the instructional team.
#
# ToDo: Change the words "hawkid" between the two double quote marks
# to match your own hawkid. Your hawkid is the "login identifier" you use
# to login to all University services, like `https://myUI.uiowa.edu/'
#
#
# Note: we are not asking for your password, just the login
# identifiers: for example, mine is "sriram".
#
###############################################################################
def signed():
    return(["tclawrence"])


###############################################################################
#
# Specification: Reads information from the files "miles.txt" and loads all the 
# data from the file into a giant dictionary and returns this dictionary. The 
# organization of this dictionary has been specified in detail in the Project 2 handout. 
# If, for some reason, "miles.txt" is missing, your function should gracefully
# finish, returning the empty dictionary {}.
# 
###############################################################################
def loadData():
    
    tempList = []
    keyList = []
    milesDict = {}
    distanceList = [[]]
    currentString = ""
    isDistance = False
    currentNumList = []
    
    f = open("miles.txt", "r")
    for line in f:
        
        tempList = []
        if (str(line))[0].isalpha() == True:
          isDistance = False
          for ch in line:
              if ch == ',' or ch == '[' or ch == ']' or ch =='\n':
                  tempList.append(currentString)
                  currentString = ""
              else:
                  currentString += ch
        elif (str(line))[0].isdigit() == True:
            isDistance = True
            currentNum = ""
            for ch in line:
                if ch.isdigit():
                    currentNum += ch
                elif ch == " ":
                    currentNumList.append(int(currentNum))
                    currentNum = ""
            currentNumList.append(int(currentNum))  
           
        else:
            isDistance = False
        if(isDistance != True and len(currentNumList) != 0):
            distanceList.append(currentNumList)
            currentNumList = []
        if len(tempList)!= 0:     
            tempList.append(currentString)
            key =  tempList[0] + tempList[1]
            keyList.append(key)
            cords = [int(tempList[2]), int(tempList[3])]
            pop = int(tempList[4])
            milesDict[key] = [cords, pop]
            
 
    for i in range(len(milesDict)):
        currentDistance = 0
        distanceDictionary = {}
        for x in range(len(milesDict)):
            if x < i:
                currentDistance = distanceList[i][i-x-1]
            elif x == i:
                continue
                currentDistance = 0
            elif x > i:
                currentDistance = distanceList[x][x-i-1]
            
            distanceDictionary[keyList[x]] = (currentDistance)
          
        milesDict[keyList[i]].append(distanceDictionary)
    
    f.close()
    
    
    return milesDict
         
###############################################################################
#
# Specification: takes the dictionary that contains all the information associated 
# with the cities and a particular city name and returns the coordinates (which is a 
# list of 2 integers) of the given city. If, for some reason, cityName is not a key
# in cityDataDict, it returns None.
#
###############################################################################
def getCoordinates(cityDataDict, cityName):
    
    if cityName in cityDataDict:
        return cityDataDict[cityName][0]
    else:
        return None
    

###############################################################################
#
# Specification: takes the dictionary that contains all the information associated 
# with the cities and a particular city name and returns the population (which is a 
# positive integer) of the given city. If, for some reason, cityName is not a key
# in cityDataDict, it returns None.
#
###############################################################################
def getPopulation(cityDataDict, cityName):
   
    if cityName in cityDataDict:
        return cityDataDict[cityName][1]
    else:
        return None

###############################################################################
#
# Specification: takes the dictionary that contains all the information associated 
# with the cities and two city names and returns the distance (an integer) 
# between cities cityName1 and cityName2. If cityName1 and cityName2 are identical, 
# it returns 0. If either cityName1 or cityName2 are not in cityDataDict, it returns
# None.
#
###############################################################################    
def getDistance(cityDataDict, cityName1, cityName2):
    
    if cityName1 in cityDataDict and cityName2 in cityDataDict and (cityName1 != cityName2):
        return cityDataDict[cityName1][2][cityName2]
    elif cityName1 == cityName2:
        return 0
    else:
        return None

###############################################################################
#
# Specification: The function takes 3 paramaters:
#    
# cityDataDict: the dictionary that contains all the information associated 
# with the cities
# 
# cityName: is a name of a city
#
# r: is a non-negative floating point number
#
# The function returns a list of cities at distance at most r from the given city,
# cityName. This list can contain the names of cities in any order. If cityName is
# not a key in cityDataDict, the function should return None.
#
###############################################################################
def nearbyCities(cityDataDict, cityName, r):
    cityList = []
    if cityName not in cityDataDict:
        return None
    else:
        cityList.append(cityName)
        for city in (cityDataDict[cityName][2]):
            if getDistance(cityDataDict, cityName, city) <= r:
                cityList.append(city)
    return cityList
            
