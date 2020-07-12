x = 70
y = 75
z = 80
if x > y:
    if x > z:
        print(f'x({x}) is bigger than y({y}) and z({z})')
    else:
        print(f'z({z}) is bigger than x({x}) and y({y})')
else:
    if y > z:
        print(f'y({y}) is bigger than x({x}) and z({z})')
    else:
        print(f'z({z}) is bigger than x({x}) and y({y})')

if z < y:
    k = 1000000

print('value of k is {1}'.format(x, k))
