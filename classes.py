class Myclass:
    def __init__(self, name, age):
        self._name = name
        self._age =  age

    def get_name(self):
        return self._name


    def set_name(self, new_name):
        self._name = new_name



james = Myclass('james', 20)

print(james.get_name())