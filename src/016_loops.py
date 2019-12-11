# for Loop
primeArray = [1, 3, 5, 7]
for prime in primeArray:
    print(prime)

print("---------------------------")

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

print("---------------------------")

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

print("---------------------------")

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

print("---------------------------")

# while Loops
# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

print("---------------------------")

# break and continue Loops
# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

print("---------------------------")

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)