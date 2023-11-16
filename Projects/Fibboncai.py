var1 = input("How many Fibonnaci numbers do you want? ")
var2 = int(0)
var3 = int(1)
var5 = 1
if int(var1) == 1:
    print(0)
elif int(var1) == 2:
    print(0)
    print(1)
else:
    var1 = int(var1) - 3
    print(0)
    print(1)
    print(1)
    for i in range(int(var1)):
        var4 = var3
        var3 = var3 + var5
        print(var3)
        var5 = var4