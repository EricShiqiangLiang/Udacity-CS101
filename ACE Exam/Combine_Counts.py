"""
Define a function, combine_counts(<dict 1>, <dict 2>), that takes two dictionaries as its inputs 
and modifies the first input dictionary to incorporate counts in the second input dictionaries.  
You may assume that all of the keys in both input dictionaries are strings and all of the values are numbers.  
Each key, <k, v>, that is in <dict 2> but not in the input <dict 1> 
should be added to <dict 1> with the same value as in <dict 2>.  
If a key occurs in both dictionaries, the value associated with that key in <dict 1> 
should be the sum of the original value in <dict 1> and the value associated with that key in <dict 2>.  
Note that <dict 2> should not be modified by combine_counts.

See the tests below
"""
def combine_counts(d1, d2):
    for key in d2:
        if key in d1:
            d1[key] = d1[key] + d2[key]
        else:
            d1[key] = d2[key]

def test():
	d1 = {'a': 1, 'b': 2, 'c': 3}
	d2 = {'a': 2, 'd': 4}
	combine_counts(d1, d2)
	print d1 == {'a': 3, 'b': 2, 'c': 3, 'd': 4}
	combine_counts(d1, d2)
	print d1 == {'a': 5, 'b': 2, 'c': 3, 'd': 8}

test()