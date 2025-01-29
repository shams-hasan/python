# find two numbers in arr that add up to target (similar to TwoSum leetcode problem)

def findSums(arr, k):
    map = {}
    for i, n in enumerate(arr):
        diff = k - n
        if diff in map:
            return (map[diff], i)
        map[n] = i

print(findSums([10, 15, 3, 7], 17) )
