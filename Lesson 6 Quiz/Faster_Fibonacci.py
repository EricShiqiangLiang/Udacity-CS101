#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).


def fibonacci(n):
    res0 = 0
    res1 = 1
    for i in range(0, n):
        res0, res1 = res1, res0 + res1
    return res0




print fibonacci(36)
#>>> 14930352