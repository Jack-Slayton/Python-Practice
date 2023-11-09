import random

with open('/workspaces/Python-Practice/Projects/SOWPODS.txt', 'r') as f:
  line = f.readline()
  while line:
    line = f.readline()
print(line)
print("HANGMAN")
print(" ______")
print("/     |")
print("|     |")
print("|     ~")
print("|     ()")
print("|    \|/")
print("|     /\ ")
print("|      ")
print("\________")