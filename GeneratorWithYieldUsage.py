def main():
    for i in inclusive_range(25):
        print(i, end=' ')
    print()


def inclusive_range(*args):
    start = 0
    step = 1
    numargs = len(args)
    if (numargs <= 0):
        print('Error: Invalid args passed')
    elif (numargs == 1):
        stop = args[0]
    elif (numargs == 2):
        start = args[0]
        stop = args[1]
    elif (numargs == 3):
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        print('Error: More than required number of args passed')

    i = start
    while i <= stop:
        yield i
        i += step


if __name__ == '__main__':
    main()
