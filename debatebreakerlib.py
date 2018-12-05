
"""
Spyder Editor

This is a temporary script file.
"""
def bubbleSort (array):
    for i in range (0, len(array)):
        for j in range (0, len(array)-1):
            if array [j]>array[j+1]:
                temp = array [j+1]
                array [j+1] = array [j]
                array [j] = temp
    return array



    
 

