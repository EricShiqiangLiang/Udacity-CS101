# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    h= []
    for n in range(0, nbuckets):
        h.append([])
    return h

print make_hashtable(3)
#Expected result for 5: [[], [], [], [], []]  
