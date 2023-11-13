word = "GATOLATOUS"
var1 = len(word)


livesleft = str("6")
guess = str.capitalize(input("What is your first guess? "))

spaces = "____________________"
spaced = spaces[0:var1]
lis = list(spaced)

var2 = 0
var3 = 1
for i in range(var1):
    if guess in word[var2:var3]:
        lis[var3 - 1] = guess
        spaced = "".join(lis)
        var2 = var2 + 1
        var3 = var3 + 1
    else:
        var2 = var2 + 1
        var3 = var3 + 1

print(spaced)
if spaced == spaces[0:var1]:
    print("one layer")
    livesleft = livesleft - 1
else:
    print("Corect")
print("You have " + livesleft + " lives left.")

lis = list(spaced)
guess = str.capitalize(input("What is your guess? "))

var2 = 0
var3 = 1
for i in range(var1):
    if guess in word[var2:var3]:
        print(var3)
        lis[var3 - 1] = guess
        spaced1 = "".join(lis)
        var2 = var2 + 1
        var3 = var3 + 1
    else:
        var2 = var2 + 1
        var3 = var3 + 1

print(spaced)
if spaced == spaced:
   print("second layer")
else:
    print("Corect")