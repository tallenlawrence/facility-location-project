#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 16:13:40 2023

@author: Sriram Pemmaraju
"""

#-------------------------------------------------------
from project2Phase1 import *
#-------------------------------------------------------

# main program
cityDataDict = loadData()

tests = []
# Test 1
tests.append(getCoordinates(cityDataDict, "Youngstown OH") == [4110, 8065])

# Test 2
tests.append(getPopulation(cityDataDict, "Youngstown OH") == 115436)

# Test 3
tests.append(getDistance(cityDataDict, "Youngstown OH", "Ravenna OH") == 34)

# Test 4
tests.append(getDistance(cityDataDict, "Youngstown OH", "Youngstown OH") == 0)

# Test 5
tests.append(getDistance(cityDataDict, "Youngstown OH", "Yankton SD") == 966)

# Test 6
tests.append(getCoordinates(cityDataDict, "Wisconsin Dells WI") == [4363, 8977])

# Test 7
tests.append(getPopulation(cityDataDict, "Wisconsin Dells WI") == 2521)

# Test 8
tests.append(getCoordinates(cityDataDict, "Ravenna OH") == [4116, 8124])

# Test 9
tests.append(getPopulation(cityDataDict, "Ravenna OH") == 11987)

# Test 10
tests.append(sorted(nearbyCities(cityDataDict, "Youngstown OH", 100.0)) == ['Ravenna OH', 'Steubenville OH','Wheeling WV', 'Youngstown OH'])

# Test 11
tests.append(getDistance(cityDataDict, "Youngstown OH",'Steubenville OH') == 60)

# Test 12
tests.append(getDistance(cityDataDict, "Youngstown OH",'Wheeling WV') == 85)

# Test 13
tests.append(sorted(nearbyCities(cityDataDict, "Waterloo IA", 200.0)) == ['Rochester MN', 'Rockford IL', 'Saint Paul MN', 'Waterloo IA'])

# Test 14
tests.append(sorted(nearbyCities(cityDataDict, "San Francisco CA", 100.0)) == ['Sacramento CA', 'San Francisco CA', 'San Jose CA', 'Santa Rosa CA', 'Stockton CA'])

# Test 15
tests.append(sorted(nearbyCities(cityDataDict, "Waco TX", 200)) == ['San Antonio TX', 'Sherman TX', 'Tyler TX', 'Waco TX'])

# Test 16
tests.append(len(nearbyCities(cityDataDict, "Waco TX",20000)) == 128)

# Test 17
tests.append(len(nearbyCities(cityDataDict, "Winston-Salem NC", 0)) == 1)

# Test 18
tests.append(("Waterloo IA" in nearbyCities(cityDataDict, "Waterbury CT", 1190)) == True)


# Test 19
tests.append(("Walla Walla WA" in nearbyCities(cityDataDict,"Waterbury CT", 1190)) == False)

# Test 20
tests.append(getDistance(cityDataDict, "Valdosta GA", "Valley City ND") == 1648)

# Test 21
tests.append(getDistance(cityDataDict, "Tampa FL", "Tallahassee FL") == 245)

# Test 22
tests.append((getCoordinates(cityDataDict, "Utica NY")[0] > getCoordinates(cityDataDict, "Waco TX")[0]) == True)

# Test 23
tests.append(sorted(nearbyCities(cityDataDict, "Saint Johnsbury VT", 150)) == ['Rutland VT', 'Saint Johnsbury VT'])

# Test 24
tests.append(sorted([getPopulation(cityDataDict, x) for x in nearbyCities(cityDataDict, "Utica NY", 100)]) == [27861, 67972, 75632, 170105])

# Test 25
tests.append(sum([getPopulation(cityDataDict, x) for x in nearbyCities(cityDataDict, "Salisbury MD", 20000)]) == 15344591)

# Test 26
tests.append(sum([getPopulation(cityDataDict, x) for x in nearbyCities(cityDataDict, "Waco TX", 20000)]) == 15344591)

# Test 27
tests.append([x for x in nearbyCities(cityDataDict, "Salina KS", 20000) if "BC" in x] == ['Vancouver BC'])

# Test 28
tests.append(sorted([x for x in nearbyCities(cityDataDict, "Salina KS", 20000) if x.startswith("San")]) == ['San Angelo TX', 'San Antonio TX', 'San Bernardino CA', 'San Diego CA', 'San Francisco CA', 'San Jose CA', 'Sandusky OH', 'Santa Ana CA', 'Santa Barbara CA', 'Santa Fe NM', 'Santa Rosa CA'])

# Test 29
tests.append(sorted([x for x in nearbyCities(cityDataDict, "Salina KS", 20000) if "IA" in x]) == ['Sioux City IA', 'Waterloo IA'])


# Test 30
tests.append(len([x for x in cityDataDict.keys()]) == 128)

# Test 31
tests.append([len([y for y in cityDataDict[x][2]]) for x in cityDataDict.keys()].count(127) == 128)

# Test 32
tests.append(getPopulation(cityDataDict, "New York NY") == None)

# Test 33
tests.append(getCoordinates(cityDataDict, "Boston MA") == None)

# Test 34
tests.append(getCoordinates(cityDataDict, "Boston MA") == None)

# Test 35
tests.append(getDistance(cityDataDict, "Seattle WA", "Boston MA") == None)

# Test 36
tests.append(getDistance(cityDataDict, "Boston MA", "Yakima WA") == None)

# Test 37
tests.append(getDistance(cityDataDict, "Boston MA", "New York NY") == None)

# Test 38
tests.append(nearbyCities(cityDataDict, "Boston MA", 0) == None)

# Test 39
tests.append(nearbyCities(cityDataDict, "Boston MA", 100) == None)

# Test 40
tests.append([len(cityDataDict[k][0]) for k in cityDataDict.keys()].count(2) == 128)

# Test 41
tests.append(sorted([cityDataDict[k][0] for k in cityDataDict.keys()])[:5] == [[2672, 8005], [2734, 8253], [2795, 8245], [2881, 9701], [2942, 9850]])

# Output the test results
i = 0
for result in tests:
    if not result:
        print("Test", i + 1, "failed")
    i = i + 1
    
