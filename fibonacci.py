a, b = 0, 1
while b < 1000:
    print(b, end=' ')
    # a, b = b, a + b
    # some how above line is equivalent to below
    c = b
    b = a + b
    a = c
