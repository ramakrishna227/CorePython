from decimal import *
x = 7
print('value of x is {}'.format(x))
print(type(x))

i=.1+.1+.1-.3
print(i)

a=Decimal('.1')
b=Decimal('.3')
i=a+a+a-b
print(i)
print(type(i))

x=7>5
print(x)
print(type(x))

x = None
print(type(x))

if x:
    print(True)
else:
    print(False)

x=' '
if x:
    print(True)
else:
    print(False)
