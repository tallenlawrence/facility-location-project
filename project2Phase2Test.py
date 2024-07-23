#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:14:07 2024

@author: sriram
"""

#-------------------------------------------------------
from project2Phase2 import *
#-------------------------------------------------------

# main program
cityDataDictionary = loadData()


tests = []

# Test 1
tests.append(sorted(greedyFacilitySet(cityDataDictionary, 5000)) == ['Ravenna OH'])

# Test 2
tests.append(sorted(greedyFacilitySet(cityDataDictionary, 1000)) == ['Red Bluff CA', 'Regina SK', 'Richmond VA', 'Saint Louis MO', 'Salt Lake City UT'])

# Test 3
tests.append(sorted(greedyFacilitySet(cityDataDictionary, 500)) == ['Reading PA', 'Regina SK', 'Rock Springs WY', 'Rockford IL', 'Roswell NM', 'Saint Augustine FL', 'Salida CO', 'Salinas CA', 'Shreveport LA', 'Sioux City IA', 'Steubenville OH', 'Walla Walla WA'])

# Test 4
tests.append(sorted(greedyFacilitySet(cityDataDictionary, 200)) == ['Ravenna OH', 'Red Bluff CA', 'Regina SK', 'Rhinelander WI', 'Richmond IN', 'Richmond VA', 'Rochester NY', 'Rockford IL', 'Sacramento CA', 'Saint Augustine FL', 'Saint Paul MN', 'Salem OR', 'Salida CO', 'Salt Lake City UT', 'San Angelo TX', 'San Antonio TX', 'San Bernardino CA', 'Santa Fe NM', 'Sarasota FL', 'Schenectady NY', 'Scottsbluff NE', 'Seattle WA', 'Sedalia MO', 'Sheridan WY', 'Sherman TX', 'Shreveport LA', 'Sioux City IA', 'Spokane WA', 'Sumter SC', 'Traverse City MI', 'Tucson AZ', 'Tuscaloosa AL', 'Twin Falls ID', 'Washington DC', 'Watertown SD', 'Wichita KS', 'Williamson WV', 'Winnipeg MB'])

# Test 5
tests.append(sorted(greedyFacilitySet(cityDataDictionary, 100)) == ['Reading PA', 'Red Bluff CA', 'Regina SK', 'Reno NV', 'Richfield UT', 'Richmond IN', 'Richmond VA', 'Rock Springs WY', 'Rockford IL', 'Rocky Mount NC', 'Roswell NM', 'Rutland VT', 'Saginaw MI', 'Saint Augustine FL', 'Saint Johnsbury VT', 'Saint Joseph MI', 'Saint Joseph MO', 'Saint Louis MO', 'Saint Paul MN', 'Salem OR', 'Salida CO', 'Salina KS', 'Salinas CA', 'Salisbury MD', 'Salt Lake City UT', 'San Angelo TX', 'San Antonio TX', 'San Francisco CA', 'Sandusky OH', 'Santa Ana CA', 'Santa Barbara CA', 'Santa Fe NM', 'Sarasota FL', 'Sault Sainte Marie MI', 'Savannah GA', 'Scottsbluff NE', 'Scranton PA', 'Seattle WA', 'Sedalia MO', 'Selma AL', 'Seminole OK', 'Sheridan WY', 'Sherman TX', 'Shreveport LA', 'Sioux City IA', 'Spokane WA', 'Springfield IL', 'Springfield MA', 'Springfield MO', 'Staunton VA', 'Sterling CO', 'Steubenville OH', 'Stevens Point WI', 'Sumter SC', 'Syracuse NY', 'Terre Haute IN', 'Toronto ON', 'Traverse City MI', 'Trinidad CO', 'Tucson AZ', 'Tupelo MS', 'Twin Falls ID', 'Valdosta GA', 'Valley City ND', 'Vancouver BC', 'Vicksburg MS', 'Victoria TX', 'Waco TX', 'Walla Walla WA', 'Warren PA', 'Washington DC', 'Waterloo IA', 'Watertown SD', 'Weed CA', 'Wenatchee WA', 'West Palm Beach FL', 'Wichita Falls TX', 'Williamson WV', 'Williston ND', 'Wilmington NC', 'Winnipeg MB', 'Winston-Salem NC', 'Yakima WA'])

# Test 6
tests.append(sorted(greedyFacilitySet(cityDataDictionary, 50)) == ['Ravenna OH', 'Reading PA', 'Red Bluff CA', 'Regina SK', 'Reno NV', 'Rhinelander WI', 'Richfield UT', 'Richmond IN', 'Richmond VA', 'Roanoke VA', 'Rochester MN', 'Rochester NY', 'Rock Springs WY', 'Rockford IL', 'Rocky Mount NC', 'Roswell NM', 'Rutland VT', 'Sacramento CA', 'Saginaw MI', 'Saint Augustine FL', 'Saint Cloud MN', 'Saint Johnsbury VT', 'Saint Joseph MI', 'Saint Joseph MO', 'Saint Louis MO', 'Saint Paul MN', 'Salem OR', 'Salida CO', 'Salina KS', 'Salinas CA', 'Salisbury MD', 'Salt Lake City UT', 'San Angelo TX', 'San Antonio TX', 'San Bernardino CA', 'San Diego CA', 'San Francisco CA', 'Sandusky OH', 'Santa Ana CA', 'Santa Barbara CA', 'Santa Fe NM', 'Santa Rosa CA', 'Sarasota FL', 'Sault Sainte Marie MI', 'Savannah GA', 'Schenectady NY', 'Scottsbluff NE', 'Scranton PA', 'Seattle WA', 'Sedalia MO', 'Selma AL', 'Seminole OK', 'Sheridan WY', 'Sherman TX', 'Shreveport LA', 'Sioux City IA', 'Sioux Falls SD', 'Spokane WA', 'Springfield IL', 'Springfield MA', 'Springfield MO', 'Springfield OH', 'Staunton VA', 'Sterling CO', 'Steubenville OH', 'Stevens Point WI', 'Sumter SC', 'Swainsboro GA', 'Syracuse NY', 'Tallahassee FL', 'Tampa FL', 'Terre Haute IN', 'Texarkana TX', 'Toledo OH', 'Topeka KS', 'Toronto ON', 'Traverse City MI', 'Trenton NJ', 'Trinidad CO', 'Tucson AZ', 'Tulsa OK', 'Tupelo MS', 'Tuscaloosa AL', 'Twin Falls ID', 'Tyler TX', 'Uniontown PA', 'Utica NY', 'Valdosta GA', 'Valley City ND', 'Vancouver BC', 'Vicksburg MS', 'Victoria TX', 'Vincennes IN', 'Waco TX', 'Walla Walla WA', 'Warren PA', 'Washington DC', 'Waterbury CT', 'Waterloo IA', 'Watertown NY', 'Watertown SD', 'Waukegan IL', 'Waycross GA', 'Weed CA', 'Wenatchee WA', 'West Palm Beach FL', 'Wichita Falls TX', 'Wichita KS', 'Williamson WV', 'Williamsport PA', 'Williston ND', 'Wilmington DE', 'Wilmington NC', 'Winchester VA', 'Winnipeg MB', 'Winston-Salem NC', 'Wisconsin Dells WI', 'Yakima WA', 'Yankton SD'])

# Test 7
tests.append(sorted(greedyFacilitySet(cityDataDictionary, 10)) == ['Ravenna OH', 'Reading PA', 'Red Bluff CA', 'Regina SK', 'Reno NV', 'Rhinelander WI', 'Richfield UT', 'Richmond IN', 'Richmond VA', 'Roanoke VA', 'Rochester MN', 'Rochester NY', 'Rock Springs WY', 'Rockford IL', 'Rocky Mount NC', 'Roswell NM', 'Rutland VT', 'Sacramento CA', 'Saginaw MI', 'Saint Augustine FL', 'Saint Cloud MN', 'Saint Johnsbury VT', 'Saint Joseph MI', 'Saint Joseph MO', 'Saint Louis MO', 'Saint Paul MN', 'Salem OR', 'Salida CO', 'Salina KS', 'Salinas CA', 'Salisbury MD', 'Salt Lake City UT', 'San Angelo TX', 'San Antonio TX', 'San Bernardino CA', 'San Diego CA', 'San Francisco CA', 'San Jose CA', 'Sandusky OH', 'Santa Ana CA', 'Santa Barbara CA', 'Santa Fe NM', 'Santa Rosa CA', 'Sarasota FL', 'Sault Sainte Marie MI', 'Savannah GA', 'Schenectady NY', 'Scottsbluff NE', 'Scranton PA', 'Seattle WA', 'Sedalia MO', 'Selma AL', 'Seminole OK', 'Sheridan WY', 'Sherman TX', 'Shreveport LA', 'Sioux City IA', 'Sioux Falls SD', 'South Bend IN', 'Spokane WA', 'Springfield IL', 'Springfield MA', 'Springfield MO', 'Springfield OH', 'Staunton VA', 'Sterling CO', 'Steubenville OH', 'Stevens Point WI', 'Stockton CA', 'Stroudsburg PA', 'Sumter SC', 'Swainsboro GA', 'Syracuse NY', 'Tacoma WA', 'Tallahassee FL', 'Tampa FL', 'Terre Haute IN', 'Texarkana TX', 'Toledo OH', 'Topeka KS', 'Toronto ON', 'Traverse City MI', 'Trenton NJ', 'Trinidad CO', 'Tucson AZ', 'Tulsa OK', 'Tupelo MS', 'Tuscaloosa AL', 'Twin Falls ID', 'Tyler TX', 'Uniontown PA', 'Utica NY', 'Valdosta GA', 'Valley City ND', 'Vancouver BC', 'Vicksburg MS', 'Victoria TX', 'Vincennes IN', 'Waco TX', 'Walla Walla WA', 'Warren PA', 'Washington DC', 'Waterbury CT', 'Waterloo IA', 'Watertown NY', 'Watertown SD', 'Waukegan IL', 'Wausau WI', 'Waycross GA', 'Weed CA', 'Wenatchee WA', 'West Palm Beach FL', 'Wheeling WV', 'Wichita Falls TX', 'Wichita KS', 'Williamson WV', 'Williamsport PA', 'Williston ND', 'Wilmington DE', 'Wilmington NC', 'Winchester VA', 'Winnipeg MB', 'Winston-Salem NC', 'Wisconsin Dells WI', 'Worcester MA', 'Yakima WA', 'Yankton SD', 'Youngstown OH'])

for i in range(len(tests)):
    if not tests[i]:
        print("Test", i+1, "failed")