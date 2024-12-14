   # O(N) SOLUTION

    def twoSum2(nums, target):
        map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff], i]
            map[n] = i
        return
    
    print(twoSum1([1,2,3], 3))
