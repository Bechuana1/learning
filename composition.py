class Car:
    def __init__(self, model, speed, engine):
        self._model = model
        self._speed = speed
        self._engine = engine

    def get_speed(self):
        return self._speed

    def set_speed(self, new_speed):
        self._speed = new_speed


    def set_model(self,new_model):
        self._model = new_model

    def get_model(self):
        return self._model



class Engine:
    def __init__(self, horsepower, torque, capacity):
        self._horsepower = horsepower
        self._torque = torque
        self._capacity = capacity


    def describe(self):
        return "this car has a " + self._capacity+ " liter v6 engine capable of producing "+self._horsepower +"HP and "+self._torque+"NM of tourque "



# ducati = Engine('240', '560', '3' )
# print(ducati.describe())

engine = Engine('240', '560', '3' )
car = Car('Aston martin DB12', '240', engine)

