def main():
    kitten('meow', 'grr', 'purr')


def kitten(*arg):
    if len(arg):  # anything greater than 0 is true
        for s in arg: # we can also use else with for loop and it will get executed post for loop
            print(s)
    else:
        print('Meew')


if __name__ == '__main__': main()
