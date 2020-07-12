class Duck:
    hello = 'Helloooo'

    def quack(self):
        print('Quack!!')
        print(self.hello)

    def walk(a):
        print()
        print('Walk like duck')
        print(a.hello)
        print('hello "{0:>25}"'.format('ram'))
        print()
        a = 5
        b = 6
        print(f'hello {a} {b}')


def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    print(type(donald))


if __name__ == '__main__': main()
