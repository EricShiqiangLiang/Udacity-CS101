"""
Define a Python procedure, closer_match(a, b, c), 
that takes three numbers as its inputs, and returns whichever of b or c is closer to a.  
The distance between two numbers is the absolute value of their difference.  
If b and c are equally close to a, either value may be returned.
"""
def closer_match(a, b, c):
    if abs(b-a) < abs(c-a):
        return b
    if abs(b-a) > abs(c-a):
        return c
    if abs(b-a) == abs(c-a):
        return b



# Example tests. All should print True, if your procedure definition is correct

print closer_match(3, 4, 5) == 4
print closer_match(5, 3, 7) == 3 or closer_match(5, 3, 7) == 7
print closer_match(5, 4, 7) == 4