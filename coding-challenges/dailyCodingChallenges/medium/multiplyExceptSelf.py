# multiply each element to every other number in the list, return products in new list

def multiplyExceptSelf(arr):  
    products = []
    for i in range(len(arr)):
        product = arr[0]
        for j in range(1, len(arr)):
            if i == j:
                continue
            else: 
                product *= arr[j] 
            products.append(sum)
    return products
print(multiplyExceptSelf([1, 2, 3, 4, 5])) # [120, 60, 40, 30, 24]