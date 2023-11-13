word = "GATOLATOUS"
var1 = len(word)

guess = str.capitalize(input("What is your first guess? "))

spaces = "____________________"
spaced = spaces[0:var1]
print(spaced)
lis = list(spaced)
print(lis)


var2 = 0
var3 = 1
for i in range(var1):
    if guess in word[var2:var3]:
        print(var3)
        lis[var3 - 1] = guess
        spaced = "".join(lis)
        var2 = var2 + 1
        var3 = var3 + 1
    else:
        var2 = var2 + 1
        var3 = var3 + 1

print(spaced)