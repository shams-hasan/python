class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return freqMap(s) == freqMap(t) # check whether the dict mappings are the same for s and t

def freqMap(string): # parameter: our string 

    dict = {}

    for c in string: # loop through string
        dict[c] = dict.get(c, 0) + 1 # update character to its count
    return dict