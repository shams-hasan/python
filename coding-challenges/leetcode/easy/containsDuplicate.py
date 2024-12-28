# solved using a set to avoid duplicates

class Solution(object):
    def containsDuplicate(nums):

        hashset = set() # initializing a hashset
        for num in nums: # loop through nums array
            if num not in hashset: # If num hasn't been added to the set
                hashset.add(num)
            else: # num has already been added, so there exists a duplicate
                return True
            
        return False

print(Solution.containsDuplicate([1,2,1,9,0,8])) # True       
print(Solution.containsDuplicate([5,3,1,9,0,8])) # False       
