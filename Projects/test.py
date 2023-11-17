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
dettype = Product
print(dettype)
if ".0" in Product:
    print("ok")
else:
    print("NOT OK NOT OK")
if str(Product[-1:]) == 0:
    Product = int(Product + 1 - 1)
else:
    Product = Product
print(Product)