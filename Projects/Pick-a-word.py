import random

with open('/workspaces/Python-Practice/Projects/SOWPODS.txt', 'r') as f:
  word = random.choice(open("/workspaces/Python-Practice/Projects/SOWPODS.txt").readlines())
life = 0
var1 = len(word)
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
spaces = "________________________________"
print(spaces[0:var1])

oneg = input("What is your first guess? ")

if str.capitalize(oneg) in word:
  print("Correct!")
else:
  print("Wrong!")
  life = int(life) + 1
  print(life)


print(" ______")
print("/     |")
print("|     |")
print("|     ~")
print("|     ()")
print("|    \|/")
print("|     /\ ")
print("|      ")
print( )
