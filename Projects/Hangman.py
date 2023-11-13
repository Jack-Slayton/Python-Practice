import random

#pick the word and set life
with open('/workspaces/Python-Practice/Projects/SOWPODS.txt', 'r') as f:
  word = random.choice(open("/workspaces/Python-Practice/Projects/SOWPODS.txt").readlines())
life = 0
var1 = len(word)
#Welcome
print(word)
print("Welcome to Hangman:")
print(" ______")
print("/     |")
print("|     |")
print("|     ")
print("|     ")
print("|    ")
print("|      ")
print("|      ")
print( )
#Set spaces and print
spaces = "________________________________________"
spaced = spaces[0:var1]
print(spaced)
lis = list(spaced)
print(lis)
#First guess
guess = str.capitalize(input("What is your first guess? "))

var2 = 0
var3 = 1
for x in word:
    if guess in word[var2:var3]:
        print(var3)
        lis[var3] = guess
        var2 = var2 + 1
        var3 = var3 + 1
    else:
        var2 = var2 + 1
        var3 = var3 + 1

print(lis)
spaced = "".join(lis)
print(spaced)
        
print(" ______")
print("/     |")
print("|     |")
print("|     ~")
print("|     ()")
print("|    \|/")
print("|     /\ ")
print("|      ")
print( )
