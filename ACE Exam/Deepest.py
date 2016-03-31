"""
Define a function, deepest(<list>), that takes as input a list (which may be arbitrarily nested), 
and returns the deepest element in the list.  
The deepest element is the element which is inside the most lists.  
If there are multiple elements with the same highest depth, your function may return any of those elements.

For example,
	deepest([1, [2, [3, [4]]], [5, [6, [7, [8, [9]]]]]]) => 9
	deepest([1, [2, [3, [4, 5]]], [[3]]]) => 4 or 5
	deepest([[1], [[2]], [[[3]]], [[[[4]]]]]) => 4

"""
def is_list(p):
    return isinstance(p, list)

def has_list(p):
    for element in p:
        if is_list(element):
            return True
    return False
    
def one_level(p):
    res=[]
    for element in p:
        if is_list(element):
            for el in element:
                res.append(el)
    return res

def deepest(p):
    while has_list(p):
        p = one_level(p)
    return p.pop()
    
print deepest([1, [2, [3, [4]]], [5, [6, [7, [8, [9]]]]]])
print deepest([1, [2, [3, [4, 5]]], [[3]]])
print deepest([[1], [[2]], [[[3]]], [[[[4]]]]])  