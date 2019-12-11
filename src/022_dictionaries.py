phonebook = {}
phonebook["Hakan"] = 5321234567
phonebook["Burcu"] = 5359876543
phonebook["Ziya"] = 5424567890
phonebook["Hale"] = 5323456789
print(phonebook)

print("------------------------------")

phonebook = {
    "Hakan" : 5321234567,
    "Burcu" : 5359876543,
    "Ziya" : 5424567890,
    "Hale" : 5323456789
}
print(phonebook)

print("------------------------------")

# Iterating over dictionaries
phonebook = {
    "Hakan" : 5321234567,
    "Burcu" : 5359876543,
    "Ziya" : 5424567890,
    "Hale" : 5323456789
}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

print("------------------------------")

# Removing a value
phonebook = {
    "Hakan" : 5321234567,
    "Burcu" : 5359876543,
    "Ziya" : 5424567890,
    "Hale" : 5323456789
}
del phonebook["Hale"]
print(phonebook)

phonebook = {
    "Hakan" : 5321234567,
    "Burcu" : 5359876543,
    "Ziya" : 5424567890,
    "Hale" : 5323456789
}
phonebook.pop("Ziya")
print(phonebook)