def score_throws(radii):
    
    points = 0 # track points
    
    # consider empty array
    if (not radii):
        return 0
    
    # consider all nums are less than 5
    if (all(num < 5 for num in radii)): 
        points += 100

    # add on points rewarded for each number
    for number in radii:
        if number >= 5 and number <= 10:
            points += 5

        elif (number < 5):
            points += 10

    return points

