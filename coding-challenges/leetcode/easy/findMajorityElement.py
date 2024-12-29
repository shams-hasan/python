class Solution(object):
    def majorityElement(nums):

        majority = len(nums) / 2
        map = {}

        for num in nums: 
            if num not in map:
                map[num] = 1 # set a count of 1 to the element if not already in map
            else:
                map[num] += 1 # otherwise increment the count

        for key in map.keys(): # loop through hashmap keys of elements
            if map[key] > majority: # if the count of element is greater than len(nums) / 2
                return key # return the element
            

print(Solution.majorityElement([1, 2, 2, 5, 6, 2, 2])) # 2