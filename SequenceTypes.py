myList = [1, 2, 3, 4, 5] #List in python are mutable and can have variable length
for i in myList:
    print(f'value is {i}')

myList[2] = 42
print()
for i in myList:
    print(f'value is {i}')

myTuple = (1, 2, 3, 4, 5) # Tuple in python is immutable and has fixed length
for i in myTuple:
    print(i)
print('length is ' + str(len(myTuple)))
print('value at 3 is ' + str(myTuple[2]))

# myTuple[2]=42
print(myTuple)

x = range(5, 50, 5)
for i in x:
    print(i)
print(type(x))
print(x[2])
x = list(x)
x[3] = 43
print()
print('Modified list is ')
for i in x:
    print(i)

x = {'one': 1, 'two': 2, 'three': 3}
for i in x:
    print(i)  # This prints only keys of a dictionary

# To print both keys and values in a dictionary, we need to use items()

for k, v in x.items():
    print(f'"{k}" is Key and "{v}" is value')
print(type(x))

x['three'] = 42
for k, v in x.items():
    print(f'"{k}" is Key and "{v}" is value')

x[4] = 'four'
for k, v in x.items():
    print(f'"{k}" is Key and "{v}" is value')
