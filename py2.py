class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, make):
        self._make = make

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

my_car = Car("Toyota", "Camry", 2020)
make = my_car.make

my_car.make = "Honda"
make = my_car.make