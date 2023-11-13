#currently using to test FOR loop for hangman
var1 = 0
for i in range(50):
    var1 = var1 + 1
    print(var1)

S = "GATOLATOUS"
a = ""
for i in S:
    if i not in a:
        a += i
print(len(a))