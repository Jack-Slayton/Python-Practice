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
print(spaces[0:var1])

#First guess
guess = str.capitalize(input("What is your first guess? "))

if str.capitalize(guess) in word:
  print("Correct!")
  point = word.rfind(guess) + 1
  print(point)
else:
  print("Wrong!")
  life = int(life) + 1
  lifeleft = 6 - int(life)
  print("You have" + lifeleft + "lives remaining.")


print(" ______")
print("/     |")
print("|     |")
print("|     ~")
print("|     ()")
print("|    \|/")
print("|     /\ ")
print("|      ")
print( )
