words = ['one', 'two', 'three', 'four', 'five']
n = 0
print('Using while loop')
while n < 5:
    print(words[n])
    n = n + 1

print('\n')
print('Using for loop')

for i in range(5):
    print(words[i], i)

print()
print('For another variation')

for i in words:
    print(i)
