from typing import *

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        list = set(nums) # set to remove duplicates
        return [i for i in range(1, len(nums) + 1) if i not in list]



