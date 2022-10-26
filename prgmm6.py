x = 5
y = 10
print("x=", x, " y=", y, sep="")
print("x=", y , " y=", x, sep="")

x, y = y, x
print("x=", x, " y=", y, sep="") # varianti
tmp = x
x = y
y = tmp
print("x=", x, " y=", y, sep="") #drug variant

