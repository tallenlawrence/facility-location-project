#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 19:20:46 2024

@author: sriram
"""

# Test 1
# I know that with r = 5000, there is a solution to facility location with one city.
# I know this because the greedy algorithm finds one such solution. In this test I 
# use the brute-force optimal algorithm to find a solution with one city for r = 5000.
#
# oneSolution = ['Ravenna OH', 'Red Bluff CA']
# optimalFacilitySet(cityDataDictionary, 5000, oneSolution)
# Out[149]: ['Youngstown OH']


# Test 2
# I know that with r = 10, every city needs to host a facility. So the brute-force optimal
# algorithm should definitely not be able to find a solution with one facility, for r = 10.
#
# optimalFacilitySet(cityDataDictionary, 10, oneSolution)
# Out[150]: []

# Test 3
# The greedy algorithm finds a solution of size 5 for r = 1000. Can we improve on this by
# using the brute-force algorithm? It turns out that yes, the brute-force algorithm can
# find a solution of size 4. I implemented a "helper" function called feasible, that checks
# if a given solution is feasible and I used it to check that the solution produced
# by the brute-force algorithm is feasible.
#
# oneSolution = greedyFacilitySet(cityDataDictionary, 1000)
# oneSolution
# Out[152]: 
# ['Saint Louis MO',
#  'Salt Lake City UT',
#  'Richmond VA',
#  'Regina SK',
#  'Red Bluff CA']
# optimalFacilitySet(cityDataDictionary, 1000, oneSolution)
# Out[153]: ['Youngstown OH', 'Yankton SD', 'Vicksburg MS', 'Stockton CA']
# feasible(cityDataDictionary, ['Youngstown OH', 'Yankton SD', 'Vicksburg MS', 'Stockton CA'], 1000)
# Out[154]: True


# Test 4
# The greedy algorithm finds a solution of size 3 for r = 1200. Can we improve on this by
# using the brute-force algorithm? It turns out that yes, the brute-force algorithm can
# find a solution of size 2. I implemented a "helper" function called feasible, that checks
# if a given solution is feasible and I used it to check that the solution produced
# by the brute-force algorithm is feasible.
#
# oneSolution = greedyFacilitySet(cityDataDictionary, 1200)
# oneSolution
# Out[156]: ['Springfield IL', 'Rock Springs WY', 'Reading PA']
# optimalFacilitySet(cityDataDictionary, 1200, oneSolution)
# Out[157]: ['Vincennes IN', 'Twin Falls ID']
# feasible(cityDataDictionary, ['Vincennes IN', 'Twin Falls ID'] , 1200)
# Out[158]: True

# Test 5
# If the solution produced in Test 4 by the brute-force algorithm is indeed optimal then
# the brute-force algorithm should not be able to generate anything smaller.
#
# optimalFacilitySet(cityDataDictionary, 1200, ['Vincennes IN', 'Twin Falls ID'])
# Out[159]: []


# Test 6
# The greedy algorithm finds a solution of size 5 for r = 900. Can we improve on this by
# using the brute-force algorithm? It turns out that yes, the brute-force algorithm can
# find a solution of size 4. I implemented a "helper" function called feasible, that checks
# if a given solution is feasible and I used it to check that the solution produced
# by the brute-force algorithm is feasible.
#
# oneSolution = greedyFacilitySet(cityDataDictionary, 900)
# oneSolution
# Out[161]: ['Richmond IN', 'Twin Falls ID', 'Roswell NM', 'Regina SK', 'Roanoke VA']
# optimalFacilitySet(cityDataDictionary, 900, oneSolution)
# Out[162]: ['Yankton SD', 'Winston-Salem NC', 'Wichita Falls TX', 'Weed CA']
# feasible(cityDataDictionary, ['Yankton SD', 'Winston-Salem NC', 'Wichita Falls TX', 'Weed CA'], 900)
# Out[163]: True

# Test 7
# If the solution produced in Test 6 by the brute-force algorithm is indeed optimal then
# the brute-force algorithm should not be able to generate anything smaller.
#
# optimalFacilitySet(cityDataDictionary, 900, ['Yankton SD', 'Winston-Salem NC', 'Wichita Falls TX', 'Weed CA'])
# Out[164]: []