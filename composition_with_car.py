""" this example uses composition to create relationship between objects
    - composition allows one object to contain another object and use the fuctions of the contained objects

    in the example, we have a class Engine and an object ducati. this class contains the start() method which
    prints "engine has started"

    we also have another class car, which take in the object ducati as a parameter and also has a methos start()
    which prints "car has started"
    notice we are able to use the ducati.start() method from above class Engine"""


class Engine:
    def start(self):
        print('Engine has started')


class Car:
    def __init__(self, ducati):
        self._engine = ducati


    def start(self):
        self._engine.start()
        print('car has started')

ducati = Engine()
car = Car(ducati)
car.start()