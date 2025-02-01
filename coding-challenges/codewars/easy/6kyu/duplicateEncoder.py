# return a new string that replaces each char with:
# "(" for count == 1 in word
# ")" for count > 1 in word

def duplicate_encode(word):

    encoded = ""
    seen = set()
    duplicates = set()
    word = word.lower()
    
    for c in word:
        if c not in seen:
            seen.add(c)
        else:
            duplicates.add(c)
            
    for c in word:
        if c in duplicates:
            encoded += ")"
        else:
            encoded += "("
            
    return encoded
    