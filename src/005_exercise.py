varString = "hello"
varFloat = 6.5
varInt = 11

if varString == "hello":
    print("String: %s" % varString)

if isinstance(varFloat, float) and varFloat == 6.5:
    print("Float : %f" % varFloat)

if isinstance(varInt, int) and varInt == 11:
    print("Integer : %i" % varInt)