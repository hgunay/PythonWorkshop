class myClass:
    variable = "test"

    def function(self):
        print("inside the class.")

myObject1 = myClass()
myObject2 = myClass()

myObject2.variable = "test 123"

print(myObject1.variable)
print(myObject2.variable)

print("------------------------------")

myObject1.function()