class Animal:
    def __init__(self, type, name, sound):
        self._type = type
        self._name = name
        self._sound = sound

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound


class Car:
    def __init__(self, **kwargs):
        self._company = kwargs['company']
        self._color = kwargs['color']
        self._model = kwargs['model']

    def company(self):
        return self._company

    def color(self):
        return self._color

    def model(self):
        return self._model

def printObject(o):
    if isinstance(o, Car):
        print(f' company is {o.company()}, color is {o.color()} and model is {o.model()}')
        print()
    elif isinstance(o, Animal):
        print(f'type is {o.type()}, name is {o.name()} and sound is {o.sound()}')
        print()
    else:
        raise TypeError('Object passed is neither Animal nor Car')

def main():
    audi = Car(company='Audi', color='Red', model='Sedan')
    brio = Car(company='Honda', color='White', model='Hatchback')
    cat = Animal('Cat', 'Tommy', 'Meow')
    dog = Animal('Dog', 'BruceLee', 'Bow')

    printObject(audi)



if __name__ == '__main__':main()
