import random

response = int(input("Rock, Paper, Scissors: press 1 to choose Rock, 2 for Paper, and 3 for Scissors."))

output = int(random.randint(1,3)) 

if output == int(1):
    var2 = str("Rock")
if output == int(2):
    var2 = str("Paper")
if output == int(3):
    var2 = str("Scissors")
else:
    var2 = "no"

if response == int(1):
    var1 = str("Rock")
if response == int(2):
    var1 = str("Paper")
if response == int(3):
    var1 = str("Scissors")
else:
    var1 = "no"

print(var1)
print(output)
