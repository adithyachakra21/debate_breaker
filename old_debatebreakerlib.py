# -*- coding: utf-8 -*-
"""
@author: Owner
"""

def evenCount (array, arg, index):
    count = 0
    
    for i in range (index, len(array)):
        if array[i] == arg:
            count = count + 1
    
    if count == 1:
        return 1;    
    elif count % 2 == 0:
        return True
    else:
        return False
    
def bubbleSort (array):
    for i in range (0, len(array)):
        for j in range (0, len(array)-1):
            if array [j]>array[j+1]:
                temp = array [j+1]
                array [j+1] = array [j]
                array [j] = temp
    return array

def reduceList (array):
    output = []

    count = 0
    
    for i in range (0, len(array)-1):
        if array [i] != array [i+1]:
            output += [array[i]]
            
    output += [array [len(array)-1]]
    return output

def lowEvenSplit (array, arg, ind):
    count = 0
    output = list (array)
    #for i in range (0,len(array)):
   #     if array[i]==arg:
   #         break
    if array[ind] != arg:
        return False
      
    for k in range (ind, len(array)):
        count = count+1
        if k == len(array)-1:
            break        
        if array [k] != array [k+1]:
            break
    
    if count % 2 != 0:
        return False
            
    for j in range (ind, ind + int((count/2))):
        output [j] = output [j] + 1
        
    return output

#print (lowEvenSplit ([1,1,2,2,2,2,3,4,5,5,5,5],5,8))

def lowOddSplit (array, arg, ind):
    
    #for i in range (0,len(array)):
     #   if array[i]==arg:
      #      break
    
    output = list (array)
    count = 0
    
    if array[ind] != arg:
        return False
    
    for k in range (ind, len(array)):
        count = count + 1 
        if k == len(array)-1:
            break
        if array [k] != array [k+1]:
            break
         
    if count % 2 != 1:
        return False
        
    for j in range (ind, ind + int(count/2)):
        output [j] = output [j] + 1
    
    output [k] = output [k] + 1
    
    return output

#print (lowOddSplit([1,1,1,1,3,4,5],1,1))



    
 


