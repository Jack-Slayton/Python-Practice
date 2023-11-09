number = int(input("Gimme a random number. "))
number2 = str(number)
var1 = (str(number / 2))[-2:]

if ".5" not in str(var1):
    var2 = "even"
else:
    var2 = "odd"

if ".0" in str(var1):
    var3 = str("is")
else:
    var3 = str("is not")

if "-" not in str(number):
    var4 = str(".")
else:
    var4 = str(". Your number is negitive.")
print("Your number (" + number2 + ") is "  + var2 + ", and also " + var3 + " a mutiple of 4" + var4)