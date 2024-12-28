from typing import *

def getSingleElement(arr : List[int]) -> int:
    
    map = {}

    for num in arr: # iterate through array
        count = 0
        if ((map.get(num)) == None): # if item is not found
            map[num] = 1 # set the count of item to 1
        else:
            map[num] += 1 # otherwise, increment count of element by 1

    for item, count in map.items(): # loop through map
        if count == 1: # if there is an element with a count of 1
            return item # return that element
    

print(getSingleElement([2, 2, 1, 3, 9, 3, 9]))