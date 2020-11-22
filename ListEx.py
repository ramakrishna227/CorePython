def main():
    myList=range(10)
    print(myList)
    for i in myList: print(i)

    print()

    myList2=[i*2 for i in myList]
    for i in myList2: print(i)

    print()
    myList3=[x for x in myList if x%3!=0] # to add all the elements other than that divisable by 3
    for i in myList3: print(i)

    print()
    myList4=[(x, x**3) for x in myList] # to create a list of tuples, ** is power
    for i in myList4: print(i)

    print()
    # we can call other methods while creating list as below
    from math import pi
    myList5=[round(pi, i) for i in myList]
    for i in myList5: print(i)

    print()
    # create a dictionary
    myDict={x:x**2 for x in myList}
    print(myDict)
    for i in myDict: print(i)

    # performing op on string
    print()
    myList6=[x for x in 'superduper' if x not in 'pd']
    for i in myList6: print(i)

    print()
    mySet = {x for x in 'superduper' if x not in 'pd'}
    for i in mySet: print(i)

if __name__ == '__main__':main()