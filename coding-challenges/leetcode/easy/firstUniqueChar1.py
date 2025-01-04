## method 1: using for loops & if/else statements

class Solution(object):
    def firstUniqChar(self, s):
        unique = -1 # store index of unique character
        first_unique = {}

        for i, c in enumerate(s): # loop through string, keep track of index & char
            if c in first_unique: # if character is found in map
                first_unique[c] = -1 # then it has been repeated
            else:
                first_unique[c] = i # otherwise, set its index

        valid = [] # stores values greater than 1
        for value in first_unique.values(): # loop through values of map
            if value > -1: # if value hasnt been repeated
                valid.append(value) # add it to our valid list
                unique = min(valid) # find the minimum index
        return unique # return minimum index
            
