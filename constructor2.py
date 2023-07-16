# define class

class Cars:
    
    # define constructor

    def __init__(self, aName, aModel, aType) -> None:
        self.name = aName
        self.model = aModel
        self.type = aType
    
    # define method
    
    def car_details(self):
        print(self.name, self.model, self.type)

# creating object and passing car details during its creation

car1 = Cars("Mercedez", 2017, "Luxury")
car1.car_details() # calling method


# define object

# call function through object