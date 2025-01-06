# return positive numbers that are multiples of 3 or 5
def solution(number):
    
    return sum(0 if n < 0 else n for n in range(number) if n % 3 == 0 or n % 5 == 0 )  