symbol = int(input("What process would you like to complete? Press 1 for addition, 2 for subtraction, 3 for mutiplication, and 4 for division. "))

if symbol == 1:
    number1 = input("What is the first number you would like to add? ")
    yes = isinstance(number1, str)
    if yes == "True":
        print("Has to be a number")
    else:
        number2 = input("What is the first number you would like to add? ")
        yes = isinstance(number2, str)
        if yes == "True":
            print("Has to be a number")
        else:
            Product = float(number2) + float(number1)
            dettype = Product
            print(dettype)
            if Product[:-1] == 0:
                Product = int(Product + 1 - 1)
            else:
                Product = Product
            print(Product)
