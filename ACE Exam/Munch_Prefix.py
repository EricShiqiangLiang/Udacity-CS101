"""
Define a function, munch_prefix(p, q), 
that takes as input two lists and returns a new list containing all the elements of q 
except of any elements at the beginning of q that match the corresponding elements at the beginning of p.  

For example,

munch_prefix([1, 2, 3, 4], [5, 6]) => [5, 6]
munch_prefix([1, 2, 3, 4], [3, 4, 5]) => [3, 4, 5] 
munch_prefix([1, 2, 3, 4], [1, 2, 4, 5, 6]) => [4, 5, 6] 
munch_prefix([1, 2, 3, 4], [1, 2, 3]) => [] 

"""




"""
Note that the returned list should not share any storage with either of the input lists, 
and the input lists must not be modified by your function:

	a = [1, 2, 3]
	b = [1, 2, 3, 4, 5]
	c = munch_prefix(a, b)
	b[4] = 6
	assert c == [4, 5]
"""
def munch_prefix(p, q):
    index = 0
    if p[0] == q[0]:
        for i in range(0, min(len(q), len(p))):
            if p[i] == q[i]:
                index = index + 1
            else:
                break
        return q[index:]
    return q
            
print munch_prefix([1, 2, 3, 4], [5, 6])
print munch_prefix([1, 2, 3, 4], [3, 4, 5])
print munch_prefix([1, 2, 3, 4], [1, 2, 4, 5, 6])
print munch_prefix([1, 2, 3, 4], [1, 2, 3])     
    
    
    
    
    
    
    
    