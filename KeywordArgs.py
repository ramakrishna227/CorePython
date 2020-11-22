def main():
    myMethod1(one='ONE', two='TWO', three='THREE')
    obj = dict(four='FOUR', five='FIVE', six='SIX')  # dict keyword to define a dictionary with key-value pairs
    myMethod2(**obj)


def myMethod1(**kwargs):
    for k in kwargs:
        print('small case is: {}; BIG case is: {}'.format(k, kwargs[k]))


def myMethod2(**kwargs):
    for k in kwargs:
        print('small case is: {}; BIG case is: {}'.format(k, kwargs[k]))


if __name__ == '__main__':
    main()
