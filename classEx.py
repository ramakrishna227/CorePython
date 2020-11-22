class Duck:
    sound="quack"
    moving="swim"

    def shout(self):
        print(self.sound)

    def move(self):
        print(self.moving)

def main():
    duck=Duck()
    duck.shout()
    duck.move()

if __name__ == '__main__': main()
