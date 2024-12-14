from operator import index
# LOOP THROUGH AN ARRAY AND FIND THE INDICES OF NUMBERS THAT ADD UP TO TARGET

# PARAMS: ARR: ARRAY, TARGET: NUMBER
# RETURN: INDICES
class Solution():
    # O(N^2)
    def twoSum1(arr, target):
        for num in arr:
            for num2 in arr:
                if num + num2 == target:
                    return [arr[num], arr[num2]]


    # O(N)
    def twoSum2(nums, target):
        map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff], i]
            map[n] = i
        return
    
    print(twoSum1([1,2,3], 3))