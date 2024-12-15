# return the longest word and/or the rightmost word if word length is the same

def longest_word(string_of_words):
    
    splittedWords = string_of_words.split() # split the string into an array of words, separates by spaces 
    longestWord = splittedWords[0] # get first word
    
    while (splittedWords): # while array is not empty
        for word in splittedWords: # loop through string list
            print(word)
            if (((len(word)) > len(longestWord)) or len(word) == len(longestWord)): # if the current word is longer or same length as longestWord 
                longestWord = word # set that word equal to the longest word
        return longestWord 
        
    