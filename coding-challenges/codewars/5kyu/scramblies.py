def scramble(s1, s2):
    # mapping s1 & s2 frequencies
    s1_mapping = getMapping(s1)
    s2_mapping = getMapping(s2)
    
    # Check if s2 can be formed from s1
    for c in s2_mapping: 
        if s2_mapping[c] <= s1_mapping.get(c, 0): # compare freq of c in s2 to that of c in s1
            continue
        else:
            return False
    
    return True  


def getMapping(s):
    char_count = {}
    for c in s:
        char_count[c] = char_count.get(c, 0) + 1
    return char_count