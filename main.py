class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    def get_make(self):
        return self._make

    def set_make(self, make):
        self._make = make

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    def get_year(self):
        return self._year

    def set_year(self, year):
        self._year = year

my_car = Car("Toyota", "Camry", 2020)
make = my_car.get_make()

my_car.set_make("Honda")
make = my_car.get_make()