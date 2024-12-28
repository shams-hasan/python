# re-solved using a hashmap for practice;
# still O(n) time complexity, but slower runtime in m/s

class Solution(object):
    def containsDuplicate(nums):

        map = {}

        for num in nums: # loop through array and keep track of index and element
            if not map.get(num): # if element is not in the array
                map[num] = 1 # set a count of 1 to that element

            else: # element was found in the array already
                return True

        return False


print(Solution.containsDuplicate([1,2,1,9,0,8])) # True       
print(Solution.containsDuplicate([5,3,1,9,0,8])) # False    