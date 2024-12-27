class Solution(object):
    def isPalindrome(x):
        x = str(x) # convert x to a string 
        reversed = x[::-1] # reverse string using splicing

        if (reversed == x):
            return True
        return False
    

print(Solution.isPalindrome(121)) # True
print(Solution.isPalindrome(110)) # False