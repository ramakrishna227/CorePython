def myMethod():
    x = {"key1": "value1", 1: 2, 'N': 'Y'}
    return x


def newDict():
    x = dict(kitter='mew', T='F') # we cannot use integer keys in this method. If we want to use integer method then the way used in myMethod is best
    for z in x: print(f'{z}:{x[z]}')
    # or can be printed using below way
    print()
    for k,v in x.items():print(f'{k}:{v}')

def main():
    y = myMethod()
    for z in y: print(f'{z}:{y[z]}')
    newDict()

if __name__ == '__main__': main()
