# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 20:15:30 2018

@author: Owner
"""
from debatebreakerlib import *

def main (teams, rounds, breaks):
    
    points = []
    for i in range (0, int(teams/2)):
        points = points + [0]
        points = points + [1] #after round 1, half teams are 0, half are 1
        
    highSorted = bubbleSort (points) #works
    lowSorted = bubbleSort (points)
    
    highReduce = reduceList (highSorted) #works
    lowReduce = reduceList (lowSorted)
    
    
    indexList = []
    
   # for p in range (0, rounds):
        #first for low wins
        #for j in range (0, len(lowReduce)): #iterates through the elements
    for element in lowReduce:
        indexList += [lowSorted.index (element)]
        
    #index = lowSorted.index(lowReduce [k])
    #print (index)    
    
    for k in range (0, len(lowReduce)): 
        print ("for has started anew")
        print (lowSorted)        
        if evenCount (lowSorted, lowReduce[k], indexList[k]) == True:
            print ("even count is True") 
            lowSorted = lowEvenSplit (lowSorted, lowReduce [k], indexList [k])
            lowSorted = bubbleSort (lowSorted)
            print ("sorted is " + str (lowSorted))
             
        elif evenCount (lowSorted, lowReduce[k], indexList[k]) == 1:
            continue            #element only appears once
        
        elif evenCount (lowSorted, lowReduce[k], indexList[k]) == False and k==0:
            print ("index of k is " + str(indexList[k]))
            print ("odd count")
            lowSorted = lowOddSplit (lowSorted, lowReduce [k], indexList [k])
            lowSorted = bubbleSort (lowSorted)
            print ("sorted is " + str (lowSorted))
            
        elif evenCount (lowSorted, lowReduce[k], indexList[k]) == False and evenCount (lowSorted, lowReduce[k-1], lowSorted.index(lowReduce[k-1])) == False:
            lowSorted = lowEvenSplit (lowSorted, lowReduce [k], indexList [k+1])
            lowSorted = bubbleSort (lowSorted)
            
        elif evenCount (lowSorted, lowReduce[k], indexList[k]) == False and evenCount (lowSorted, lowReduce[k-1], lowSorted.index(lowReduce[k-1])) == True:
            lowSorted = lowOddSplit (lowSorted, lowReduce [k], indexList [k])
            lowSorted = bubbleSort (lowSorted)
            
            
        lowSorted = bubbleSort (lowSorted)
        lowReduce = reduceList (lowSorted)
            
    return lowSorted

#debug: the code will run [0,1,1,1,2,2,2,2] instead of making the end 2,2,3,3
#print (main (6,1,3))

        