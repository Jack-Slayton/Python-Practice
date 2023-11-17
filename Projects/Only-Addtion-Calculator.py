symbol = int(input("What process would you like to complete? Press 1 for addition, 2 for subtraction, 3 for mutiplication, and 4 for division. "))

#addition
if symbol == 1:
    number1 = int(input("What is the first number you would like to add? "))
    if number1 > 0:
        number2 = int(input("What is the first number you would like to add? "))
        if number2 > 0:
            product = float(number1) + float(number2)
            print(product)
        elif number2 < 0:
            product = float(number1) + float(number2)
            print(product)
        elif number2 == 0:
            product = float(number1) + float(number2)
            print(product)
        else:
            print("Must be a number.")

    elif number1 < 0:
        number2 = int(input("What is the first number you would like to add? "))
        if number2 > 0:
            product = float(number1) + float(number2)
            print(product)
        elif number2 < 0:
            product = float(number1) + float(number2)
            print(product)
        elif number2 == 0:
            product = float(number1) + float(number2)
            print(product)
        else:
            print("Must be a number.")

    elif number1 == 0:
        number2 = int(input("What is the first number you would like to add? "))
        if number2 > 0:
            product = float(number1) + float(number2)
            print(product)
        elif number2 < 0:
            product = float(number1) + float(number2)
            print(product)
        elif number2 == 0:
            product = float(number1) + float(number2)
            print(product)
        else:
            print("Must be a number.")

    else:
        print("Must be a number.")
#subtraction