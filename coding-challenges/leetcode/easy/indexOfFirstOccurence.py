class Solution(object):
    def strStr(haystack, needle):
        if needle in haystack: # if needle exists in haystack
            return haystack.index(needle) # return first occurence of the needle 
        return -1 # otherwise it doesnt exist
        

print(Solution.strStr("lastdinomovie", "dino")) # 4