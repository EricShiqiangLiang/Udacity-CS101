"""
Define a Python procedure, in_language(<string>), 
that takes as input a string and returns True 
if the input string is in the language described by the BNF grammar below 
(starting from S) and returns False otherwise. 

BNF grammar description:
S => 0 S 1 
S => 1 S 0
S => 0
"""

def in_language(string):
    if len(string) == 1:
        if int(string[0]) != 0:
            return False
        else:
            return True
    else:
        if len(string)%2 == 0:
            return False
        if int(string[len(string)/2]) != 0:
            return False
        for i in range(0, len(string)/2 - 1):
            if int(string[i]) != (1 + int(string[-1 - i])) % 2:
                return False
    return True
    
    
        
# Tests. These all should print True if your procedure is defined correctly
print in_language("00011") == True
print in_language("0") == True
print in_language("01") == False
print in_language("011") == False
print in_language("01002") == False