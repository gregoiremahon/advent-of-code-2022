#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 15:56:48 2022

@author: gregoiremahon
"""
""" https://adventofcode.com/2022/day/1 """
 
CaloriesInput = []
with open('input.txt', 'r') as InputFile:
    lines = InputFile.readlines()
    for Value in lines:
        Cal_value = Value.replace('\n', '')
        Cal_value = Cal_value.replace(" ","")
        CaloriesInput.append(Cal_value)
        
CurrentElfValue = 0
Elves_Sum_Values = []
for Calorie in CaloriesInput:
    if Calorie!= '':
        CurrentElfValue += int(Calorie)
    else:
        Elves_Sum_Values.append(CurrentElfValue)
        CurrentElfValue = 0
        
print("First Part result : " + str(max(Elves_Sum_Values))) 

TopThreeElves_Values_Sum = 0
for Value in range(0, 3):
    TopThreeElves_Values_Sum += (max(Elves_Sum_Values))
    Elves_Sum_Values.remove(max(Elves_Sum_Values))
    
print("Second Part result : " + str(TopThreeElves_Values_Sum))