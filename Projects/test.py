#currently using to test FOR loop for hangman
#var1 = 0
#for i in range(50):
#    var1 = var1 + 1
#    print(var1)

#S = "GATOLATOUS"
#a = ""
#for i in S:
#    if i not in a:
#        a += i
#print(len(a))
number2 = 4
number1 = 5
Product = str(float(number2) + float(number1))

dettype = Product[-1:]
print(dettype)
dettype2 = Product[-2:-1]
print(dettype2)
dettype3 = dettype2 + dettype
print(dettype3)
if dettype3 == ".0":
    print(Product[:-2])
else:
    print(Product)