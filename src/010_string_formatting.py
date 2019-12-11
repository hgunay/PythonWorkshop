#-------------------------------------
# %s : String
# %d : Integer
# %f : Float
# %.<number of digits>f : Fixed amount of digits
#-------------------------------------
name = "Hakan"
print("Hello, %s!" % name)

age = 34
print("%s is %d years old." % (name, age))

varList = [1,2,3]
print("A list : %s" % varList)

varFloat = 4.5
print("Floating Number : %f" % varFloat)
print("Floating Number with Fixed amount of digits : %.1f" % varFloat)