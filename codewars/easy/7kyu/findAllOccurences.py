## return list of indices where element n is found

def find_all(array, n):
    occurences = []
    
    # Iterate over the array and check for occurrences of n
    for num in range(len(array)): 
        if array[num] == n: 
            occurences.append(num) # Add the index to our list if n is found
    return occurences

