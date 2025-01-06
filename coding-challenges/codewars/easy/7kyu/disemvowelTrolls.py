# strip all vowels from a string
def disemvowel(string_):
    return "".join(char for char in string_ if char not in "aeiouAEIOU")