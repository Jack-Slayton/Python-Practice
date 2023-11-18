symbol = int(input("What process would you like to complete? Press 1 for addition, 2 for subtraction, 3 for mutiplication, and 4 for division. "))

if symbol == 1:
    number1 = input("What is the first number you would like to add? ")
    yes = isinstance(number1, str)
    if yes == "True":
        print("Has to be a number")
    else:
        number2 = input("What is the second number you would like to add? ")
        yes = isinstance(number2, str)
        if yes == "True":
            print("Has to be a number")
        else:
            Product = str(float(number2) + float(number1))
            dettype = Product[-1:]
            dettype2 = Product[-2:-1]
            dettype3 = dettype2 + dettype
            if dettype3 == ".0":
                print(Product[:-2])
            else:
                print(Product)
elif symbol == 2:
    number1 = input("What is the number you would like to subtract from? ")
    yes = isinstance(number1, str)
    if yes == "True":
        print("Has to be a number")
    else:
        number2 = input("What is the number you would like to subtract? ")
        yes = isinstance(number2, str)
        if yes == "True":
            print("Has to be a number")
        else:
            Product = str(float(number1) - float(number2))
            dettype = Product[-1:]
            dettype2 = Product[-2:-1]
            dettype3 = dettype2 + dettype
            if dettype3 == ".0":
                print(Product[:-2])
            else:
                print(Product)
elif symbol == 3:
    number1 = input("What is the number you would like to mutiply? ")
    yes = isinstance(number1, str)
    if yes == "True":
        print("Has to be a number")
    else:
        number2 = input("What is the number you would like to mutilpy? ")
        yes = isinstance(number2, str)
        if yes == "True":
            print("Has to be a number")
        else:
            Product = str(float(number1) * float(number2))
            dettype = Product[-1:]
            dettype2 = Product[-2:-1]
            dettype3 = dettype2 + dettype
            if dettype3 == ".0":
                print(Product[:-2])
            else:
                print(Product)
elif symbol == 4:
    number1 = input("What is the number you would like to divide from? ")
    yes = isinstance(number1, str)
    if yes == "True":
        print("Has to be a number")
    else:
        number2 = input("What is the number you would like to divide with? ")
        yes = isinstance(number2, str)
        if yes == "True":
            print("Has to be a number")
        else:
            Product = str(float(number1) / float(number2))
            dettype = Product[-1:]
            dettype2 = Product[-2:-1]
            dettype3 = dettype2 + dettype
            if dettype3 == ".0":
                print(Product[:-2])
            else:
                print(Product)
else:
    print("Press 1, 2, 3, or 4")