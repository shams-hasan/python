class Solution(object):
    def romanToInt(s):
        map = dict(I=1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000) # pair roman:integer
        res = 0 # stores result of roman number

        for i in range(len(s)): # loop through string

            if i + 1 < len(s) and map[s[i]] < map[s[i + 1]]: # let's take the test case IV, I < V, so we want to subtract I first
                res -= map[s[i]] # subtract I (1) from res, res is now -1

            else: # now we are left with V, and we'll add that to our result
                res += map[s[i]] # -1 + 5 = 4


        return res

print(Solution.romanToInt("IV")) # 4


