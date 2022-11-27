class Car:
    def __init__(self, model=None):
        self.__model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, obj):
        if type(obj) == str and 2<= len(obj) <=100:
            self.__model = obj



car = Car()
car.model = "Toyota"
print(car.model)