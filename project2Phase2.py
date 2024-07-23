# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:09:09 2024

@author: 18159
"""

from project2Phase1 import *
import itertools

cityDataDict = loadData()

def sortedCityList(cityDataDict):
    cityList = []
    for city in cityDataDict:
        cityList.append(city)
    return sorted(cityList)

    
def greedyFacilitySet(cityDataDict, r):
    
    #initializing variables
    served = set()
    facilityList = []
    cList = sortedCityList(cityDataDict)
    
    while len(served) < len(cityDataDict):
        
        maxUnservedCount = 0
        
        for city in cList:
          
                unservedCount = len(set(nearbyCities(cityDataDict, city, r)) - served)
                
                if unservedCount > maxUnservedCount or (unservedCount == maxUnservedCount and city < bestCity):
                    bestCity = city
                    maxUnservedCount = unservedCount
        facilityList.append((bestCity))
        served.update(nearbyCities(cityDataDict, bestCity, r))       
          
    return facilityList

def feasible(cityDataDict, facilitySet, r):
    
    for city in cityDataDict:
        if all(getDistance(cityDataDict, city, facility) > r for facility in facilitySet):
            return False
    return True

def generateSubsets(cityDataDict, r, oneSolution):
    subsetList = []
    maxLength = len(oneSolution)
   
    
    for subsetSize in range(maxLength):
        for subset in itertools.combinations(cityDataDict, subsetSize):
            if feasible(cityDataDict, subset, r):
                subsetList.append(subset)
    return subsetList
        

    
    
def optimalFacilitySet(cityDataDict, r , oneSolution):
    allSubsets = generateSubsets(cityDataDict, r, oneSolution)
    cList = sortedCityList(cityDataDict)
    minFacilities = len(oneSolution)
    optimalSet = []
        
    for subset in allSubsets:
        
        if len(subset) < minFacilities:
            
            minFacilities = len(subset)
            optimalSet = list(subset)
            
    return optimalSet
        

