# reverse all words in a string that have a length >= 5
def spin_words(sentence):
    
    array = sentence.split(" ")
    return " ".join(w[::-1] if len(w) >= 5 else w for w in array)