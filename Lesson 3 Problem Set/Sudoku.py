# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
def check_square(s):
    if len(s[0]) != len(s):
        return False
    else:
        return True

def check_column(s):
    numbers = []
    for n in range(1, len(s) + 1):
        numbers.append(n)
    for c in range(0, len(s)):
        for r in s:
            if r[c] in numbers:
                numbers.pop(numbers.index(r[c]))
        if numbers:
            return False
        for n in range(1, len(s) + 1):
            numbers.append(n)
    return True

def check_row(s):
    numbers = []
    for n in range(1, len(s) + 1):
        numbers.append(n)
    for i in s:
        for e in i:
            if e in numbers:
                numbers.pop(numbers.index(e))
        if numbers:
            return False
        for n in range(1, len(s) + 1):
            numbers.append(n)
    return True

def check_sudoku(s):
    return check_row(s) and check_column(s) and check_square(s)
    


   
print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False


