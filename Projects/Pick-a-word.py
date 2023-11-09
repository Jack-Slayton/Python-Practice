import random

with open('/workspaces/Python-Practice/Projects/SOWPODS.txt', 'r') as f:
  random_lines = random.choice(open("/workspaces/Python-Practice/Projects/SOWPODS.txt").readlines())
print(random_lines)
var1 = len(random_lines)
print(var1)
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
