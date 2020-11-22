def main():
    obj = ('one', 'two', 'three', 'four')
    hello(obj)
    hello1(*obj)


def hello(obj):
    print('in hello method')
    for s in obj:
        print(s)


def hello1(*obj):
    print('in hello1 method')
    for s in obj:
        print(s)


if __name__ == '__main__':
    main()
