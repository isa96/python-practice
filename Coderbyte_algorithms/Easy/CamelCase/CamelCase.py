'''
Camel Case from Coderbyte
'''

import re

def CamelCase(strParam):
    '''
    Have the function CamelCase(str) 
    take the str parameter being passed 
    and return it in proper camel case 
    format where the first letter of each word 
    is capitalized (excluding the first letter). 
    The string will only contain letters and some 
    combination of delimiter punctuation characters 
    separating each word.

    For example: if str is "BOB loves-coding" 
    then your program should return the string "bobLovesCoding".
    '''
    try:
        words = re.split(r'[^a-zA-z]', strParam)

        all_Capitalized = "".join(word.capitalize() for word in words)
        
        output = all_Capitalized[0].lower() + all_Capitalized[1:]

        return output

    except(AttributeError, TypeError):
        return -1

