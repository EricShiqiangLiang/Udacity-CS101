"""
Define a function, mode(<list>), that takes as input a list of strings, 
and returns the string that occurs the most times in the input list.  
You may assume the input list contains at least one element.  
If there are multiple strings that could be the mode 
(that occur the same number of times, but not other string occurs more frequently), 
your function may return any of them.

For example,
	mode(['python', 'snake', 'python', 'language']) => 'python'
	mode(['a', 'b', 'c', 'b', 'a']) => may return either 'a' or 'b'

"""
def mode(list):
    max = 0
    res = []
    for str in list:
        if list.count(str) > max:
            max = list.count(str)
            res.append(str)
    return res.pop()

print mode(['python', 'snake', 'python', 'language'])
print mode(['a', 'b', 'c', 'b', 'a'])      
print mode(['one', 'two', 'two', 'three', 'three', 'three'])   
    