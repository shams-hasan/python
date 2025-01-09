# find the int that occurs an odd number of times

def find_it(seq):
    
    freqs = {} # store map of element:count
    
    for num in seq:
        freqs[num] = 1 + freqs.get(num, 0) # increment count of element in freqs map
    
    for k in freqs.keys(): # loop through keys
        if freqs[k] % 2 == 1: # if count of key is odd
            return k # return the key (element)
    
    return -1 