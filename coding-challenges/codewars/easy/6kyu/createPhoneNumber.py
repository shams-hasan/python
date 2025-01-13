# return a string of numbers in n converted to phone-number format

def create_phone_number(n):

    string = "".join(map(str, n)) # join all elements of n into a string


    return (f"({string[0:3]}) {string[3:6]}-{string[6:11]}")