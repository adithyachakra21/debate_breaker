# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 10:36:07 2018

@author: Owner
"""

from debatebreakerlib import *

def main (teams, rounds, breaks):
    
    #error handling
    if teams <= breaks + 1:
        print ("Too many teams are breaking. Please enter a different input.")
        return "\n"
    
    points = []
    for m in range (0, int(teams)):
        points = points + [0]
               
    # In lowSorted, when a low-point team and a high-point team face, the low-point team ALWAYS wins. 
    # In highSorted, when a low-point team and a high-point team face, the high-point team ALWAYS wins. 
    highSorted = bubbleSort (points) 
    lowSorted = list(highSorted)
    
    for p in range (0, rounds):
        
        for i in range (0, int((len (lowSorted))/2)):
            
            lowSorted [2*i] += 1
            highSorted [(2*i) + 1] += 1
            
        bubbleSort (lowSorted)
        bubbleSort (highSorted)
    
    #This calculates the points needed to break in the BEST CASE scenario--for lowSorted. 
    lowcount = 1
    l = 0
    
    # This loop counts how many teams break from the teams with the lowest points.
    while lowSorted[len (lowSorted) - breaks + l] == lowSorted[len (lowSorted) - breaks + l + 1]:
        lowcount += 1  
        l = l+1
        
    lowBreak = lowSorted [len(lowSorted)-breaks]
    
    if lowSorted [len(lowSorted)-breaks] != lowSorted [len(lowSorted)-breaks-1]: 
        print ("Best case: all teams on " + str(lowBreak) + " point(s) will break. All teams with more than " + str(lowBreak) + "point(s) will also break.")
        print ("")
        
    else:
        print ("Best case: the top " + str(lowcount) + " team(s) on " + str(lowBreak) + " point(s) will break. All teams with more than " + str(lowBreak) + " point(s) will also break.")
        print ("")
    
    #This calculates the points needed to break in the WORST CASE scenario--for highSorted. 
    highcount = 1
    l = 0
    
    while highSorted[len (highSorted) - breaks + l] == highSorted[len (highSorted) - breaks + l + 1]:
        highcount += 1  
        l = l+1
        
    highBreak = highSorted [len(highSorted)-breaks]
    
    if highcount== int(1):
        print ("Worst case: all teams on " + str(highBreak) + " point(s) will break. All teams with more than " + str(highBreak) + "point(s) will also break.")
        
    else:
        print ("Worst case: the top " + str(highcount) + " team(s) on " + str(highBreak) + " point(s) will break. All teams with more than " + str(highBreak) + "point(s) will also break.")
        
    return "\n"
   

print (main(200,6,16))

            
    
