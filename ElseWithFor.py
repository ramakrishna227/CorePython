def main():
    for i in range(1, 5, 2):  # if step size is 1, it will not execute else block. This relieves us from using a boolean flag to print the contents in else block
        if (i % 2 == 0):
            print('range contains even number')
            break
    else:
        print('range does not contain even number')


if __name__ == '__main__':
    main()
