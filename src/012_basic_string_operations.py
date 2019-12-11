varString1 = "Hello World!"
varString2 = 'Hello World!'

print(varString1)
print(varString2)

print("Single quotes are ' '")
print(len(varString1))
print(len(varString2))

print(varString1.index("o"))
print(varString1.count("l"))

# [start:stop]
print(varString1[3:7])

# [start:stop:step]
print(varString1[3:7:2])
print(varString1[3:7:1])

# Reverse String
print(varString1[::-1])

# Upper and Lower
print(varString1.upper())
print(varString1.lower())

print(varString1.startswith("Hello"))
print(varString1.endswith("F#%$"))

# Split String
print(varString1.split(" "))

