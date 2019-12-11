# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth %.2f TL." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Mercedes"
car1.color = "white" 
car1.value = 120000.00

car2 = Vehicle()
car2.name = "BMW"
car2.color = "black" 
car2.value = 100000.00

# test code
print(car1.description())
print(car2.description())