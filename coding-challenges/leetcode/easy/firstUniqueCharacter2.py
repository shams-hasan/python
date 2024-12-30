## method 2: using list comprehensions 

class Solution(object):
    def firstUniqChar(self, s):
        first_unique = {}
        for i, c in enumerate(s): # loop through string, keep track of index & char
            first_unique[c] = -1 if c in first_unique else i # set char to -1 if already found in map, or to its index otherwise        
        
        valid = [v for v in first_unique.values() if v > -1] # add all indices > -1 to valid list

        if valid: # if list of valid indices is not empty
            return min(valid) # find and return the minimum index

        else: # 
            return -1

