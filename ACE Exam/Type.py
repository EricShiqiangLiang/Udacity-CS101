"""
Provide a definition of g such that the expression below evaluates to True:
"""
def g(p):
    if type(p) == int:
        return g
    if type(p) == str:
        return 1
        
    
print type(g) == type(g(1)) != type(g('alpha'))
