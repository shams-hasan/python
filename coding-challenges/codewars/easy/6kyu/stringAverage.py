def average_string(s):
        word_to_num = dict({"zero": 0, "one": 1, "two": 2 , "three": 3,
                    "four": 4, "five": 5, "six": 6, "seven": 7,
                    "eight": 8, "nine": 9})

        nums = s.split(" ")
        n = len(nums)
        num_to_word = {v: k for k, v in word_to_num.items()} # reverse mapping of word_to_num
        
        sum = 0
        for word in nums: 
            if word not in word_to_num: # if there is a word in nums > 9
                return "n/a"
            sum += word_to_num[word] # add int form of word to sum
        return num_to_word.get(sum // n, "n/a") # return average
    