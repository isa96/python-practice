'''
Even Pairs from Coderbyte
'''
import re

def EvenPairs(strParam):
    '''
    Have the function EvenPairs(str) 
    take the str parameter being passed 
    and determine if a pair of adjacent 
    even numbers exists anywhere in the string. 
    If a pair exists, return the string true, 
    otherwise return false. 
    
    For example: if str is "f178svg3k19k46" 
    then there are two even numbers at the end 
    of the string, "46" so your program should 
    return the string true. 
    
    Another example: if str is "7r5gg812" 
    then the pair is "812" (8 and 12) so your 
    program should return the string true.
    '''
    
    numbers = re.split(r'[a-zA-Z]', strParam)
    numbers = filter(None, numbers)

    for number in numbers:
        if len(number) < 2:
            continue
        
        # below checks each possible pair in number
        for index in range(1, len(number)):
            if int(number[:index])%2 == 0 and\
                int(number[index:])%2 == 0:
                return "true"

    return "false"            