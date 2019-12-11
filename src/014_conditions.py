x = 2
print(x == 2)
print(x == 3)
print(x < 3)

# Boolean Operators
name = "Hakan"
age = 34
if name == "Hakan" and age == 34 :
    print("Your name is Hakan, and you are also 34 years old.")

if name == "Hakan" or name == "Hasan" : 
    print("Your name is Hakan or Hasan")

# in Operator
if name in ["Hakan", "Hasan"] : 
    print("Your name is Hakan or Hasan")

# is Operator
x = [1,2,3]
y = [1,2,3]
print(x == y)
print(x is y)

# not Operator
print(not False)
print((not False) == (False))