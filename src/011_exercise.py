# Hello Hakan Günay. Your current balance is 1500.15 TL
varData = ("Hakan", "Günay", 1500.15)
varString = "Hello %s. Your current balance is %.2f TL"

print(varString % (varData[0] +" "+ varData[1], varData[2]))