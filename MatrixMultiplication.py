import numpy as np


x=[[1,2,3],
[4,5,6],
[7,8,9]]
y=[[3,2,1],
[6,5,4],
[9,8,7]]

result=[[0,0,0],
[0,0,0],
[0,0,0]]

# if x is i*k matrix and y is k*j
# k is moving fast in both matrices
# next fast moving in j and last moving is i
# so the order of loop is i in len x
#                         j in len y[0]
#                         k in len x[0] or len y
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j]+=x[i][k]*y[k][j]

for r in result:
    print(r)


print("\n")

#Using zip function
result1 = [[sum (a* b for a, b in zip(A_row, B_col))
        for B_col in zip(*y)]
        for A_row in x]

for r1 in result1:
    print(r1)



print("\n")

# Using vectorized implementation

result3 = [[0,0,0],
[0,0,0],
[0,0,0]]


result3=np.dot(x, y)

for r3 in result3:
    print(r3)


print("\n")

resultx=np.matmul(x,y)

print("matmul is ", resultx)