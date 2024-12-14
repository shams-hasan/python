# O(N^2)

def findSumsOfTarget(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
            
    return []
    
print(findSumsOfTarget([0,2, 4, 4, 7], 8))  

