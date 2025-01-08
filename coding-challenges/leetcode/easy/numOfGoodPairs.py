from typing import *
    
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        count = {}

        for n in nums:
            if n in count: # if number was already found
                res += count[n] # add pair to the result
            count[n] = 1 + count.get(n, 0)  # then increment count of number
        return res