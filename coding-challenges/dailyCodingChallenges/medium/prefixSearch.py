# return a list of strings with prefix of s

def isPrefix(s, stringsList):
    sSet = set()
    for string in stringsList:
        if string[0:len(s)] == s:
            sSet.add(string)

    return list(sSet)


print(isPrefix("de", ["dog", "deer", "deal"]))