# Define a procedure, is_offered(courses, course, hexamester), that returns 
# True if the input course is offered in the input hexamester, and returns 
# False otherwise.  For example,

#print is_offered(courses, 'cs101', 'apr2012')
#>>> True

#print is_offered(courses, 'cs003', 'apr2012')
#>>> False

# (Note: it is okay if your procedure produces an error if the input 
# hexamester is not included in courses.
# For example, is_offered(courses, 'cs101', 'dec2011') can produce an error.)
# However, do not leave any uncommented statements in your code which lead 
# to an error as your code will be graded as incorrect.

def is_offered(courses, course, hexamester):
     return hexamester in courses and course in courses[hexamester]





print is_offered(courses, 'cs101', 'apr2012')
#>>> True

print is_offered(courses, 'cs003', 'apr2012')
#>>> False

print is_offered(courses, 'cs001', 'jan2044')
#>>> True

print is_offered(courses, 'cs253', 'feb2012')
#>>> False
    