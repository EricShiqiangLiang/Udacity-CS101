def symmetric(s):
    if s:
        if len(s) != len(s[0]):
            return False
        col = []
        for i in range (0, len(s)):
            col.append([])
            for r in s:
                col[i].append(r[i])
        if col == s:
            return True
        return False
    else:
        return True
print symmetric([[1, 2, 3],
                 [2, 3, 4],
                 [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                 ["dog", "dog", "fish"],
                 ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                 ["dog", "dog", "dog"],
                 ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                 [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                 [2, 3, 4, 5],
                 [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                  [2,3,1]])
#>>> False