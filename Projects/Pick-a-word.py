import random

with open('/workspaces/Python-Practice/Projects/SOWPODS.txt', 'r') as f:
  word = random.choice(open("/workspaces/Python-Practice/Projects/SOWPODS.txt").readlines())
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

if oneg in word:
  print("Correct!")



print("HANGMAN")
print(" ______")
print("/     |")
print("|     |")
print("|     ~")
print("|     ()")
print("|    \|/")
print("|     /\ ")
print("|      ")
print( )
