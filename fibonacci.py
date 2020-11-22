a, b = 0, 1
while b < 1000:
    print(b, end=' ')
    # a, b = b, a + b
    # some how above line is equivalent to below
    # In python, expressions on the right hand side are evaluated before assigning the results to left hand side variables
    c = b
    b = a + b
    a = c
