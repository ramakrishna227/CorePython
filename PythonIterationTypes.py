cars=['audi','bmw','range rover']

i=0
while(i<len(cars)):
    print(cars[i])
    i+=1

print("\n")

for c in cars:
    print(c)

print("\n")

for i in range(len(cars)):
    print(cars[i])

print("\n")

for index, car in enumerate(cars):
    print(index, car)

print("\n")

for x in enumerate(cars):
    print(x[0], x[1])

print("\n")

for x in enumerate(cars, start=1):
    print(x[0], x[1])


print("\n")
prices=[1000, 2000, 5000]

for c, p in zip(cars, prices):
    print(c, p)


print("\n")

for x in zip(cars, prices):
    print(x)



print("\n")
#unzipping of below list
zippedList = [('audi', 1000),
('bmw', 2000),
('range rover', 5000)]

cars, prices=zip(*zippedList)
print(cars)
print(prices)